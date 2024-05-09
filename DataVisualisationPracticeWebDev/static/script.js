document.addEventListener("DOMContentLoaded", function () {
  const socket = io();

  socket.on("dataUpdate", function (data) {
    updateChart(data);
  });

  d3.select("#btnPowerCurve").on("click", function () {
    socket.emit("requestData", { type: "powerCurve" });
  });

  d3.select("#btnFTP").on("click", function () {
    socket.emit("requestData", { type: "FTP" });
  });

  function updateChart(data) {
    // Clear existing SVG to prevent overlap
    d3.select("#chart").select("svg").remove();
    drawChart(data); // Call drawChart to redraw with new data
  }
});

function drawChart(data) {
  const margin = { top: 20, right: 20, bottom: 30, left: 50 },
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  const svg = d3
    .select("#chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  const x = d3.scaleTime().range([0, width]);
  const y = d3.scaleLinear().range([height, 0]);

  // Parse the date / time
  const parseTime = d3.timeParse("%d-%b-%y");

  // Format the data
  data.forEach(function (d) {
    d.date = parseTime(d.date);
    d.value = +d.value;
  });

  // Scale the range of the data
  x.domain(
    d3.extent(data, function (d) {
      return d.date;
    })
  );
  y.domain([
    0,
    d3.max(data, function (d) {
      return d.value;
    }),
  ]);

  // Add the valueline path.
  const valueline = d3
    .line()
    .x(function (d) {
      return x(d.date);
    })
    .y(function (d) {
      return y(d.value);
    });

  svg
    .append("path")
    .data([data])
    .attr("class", "line")
    .attr("d", valueline)
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 2);

  // Add the X Axis
  svg
    .append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  // Add the Y Axis
  svg.append("g").call(d3.axisLeft(y));
}
