from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

# Assuming PowerCurveAnalyzer is properly imported from models
from models.power_curve import PowerCurveAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/power_curve', methods=['GET'])
def power_curve():
    return render_template('power_curve.html')

@app.route('/display_power_curve', methods=['POST'])
def display_power_curve():
    try:
        activity_type = request.form['activityType']
        start_date = request.form['startDate']
        num_days = int(request.form['numDays'])
        tested_ftp = float(request.form['testedFTP'])  # Ensure this is being captured correctly

        # Initialize PowerCurveAnalyzer
        analyzer = PowerCurveAnalyzer()  # Make sure this is initialized correctly

        # Convert start_date from string to datetime object, if necessary
        start_date = datetime.strptime(start_date, "%Y-%m-%d")

        # Call the method with all required arguments
        power_curve_data = analyzer.create_power_curve(activity_type, start_date, num_days)
        print("start_date :" + str(start_date) )
        print("Activity Type :" + str(activity_type))
        print("Number of days :" + str(num_days))
        print("Tested FTP :" + str(tested_ftp))

        print(power_curve_data)
        # Assume the plot_power_curve method doesn't require tested_ftp or handle it inside
        plot_path = 'static/power_curve.png'
        analyzer.plot_power_curve(power_curve_data, tested_ftp)  # Adjust according to actual method definition
        

        return render_template('display_power_curve.html', image_path=plot_path)

    except Exception as e:
        return f"Error processing request: {e}", 400


if __name__ == '__main__':
    app.run(debug=True)
