# Cycling Analysis (Basic and Advanced)

This directory contains two Jupyter notebooks focused on analyzing cycling performance data: **Basic Analysis** and **Advanced Analysis**. The notebooks use the `extended_activities.csv` dataset, which is available in the project repository, to explore, analyze, and visualize key metrics from cycling activities.

---

## **Introduction**

The Cycling Analysis notebooks are part of a comprehensive project aimed at understanding and improving cycling performance through data analytics. These notebooks provide insights into performance trends, calorie predictions, power output zones, and training intensities. 

Key highlights:
- Data-driven evaluation of training metrics like distance, speed, heart rate, and calories burned.
- Advanced modeling techniques to predict calories burned and identify performance clusters.
- Visualizations to uncover patterns in cycling data.

These analyses aim to support athletes and trainers in making informed decisions to enhance cycling performance.

---

## **Purpose of the Notebooks**

### **Basic Analysis**
This notebook focuses on:
- Loading, filtering, and cleaning the dataset for cycling-specific activities.
- Basic exploratory data analysis (EDA) including summary statistics and visualizations.
- Identifying trends and patterns in relative effort, average speed, and distance.
- Categorizing power output zones to understand training intensity distribution.

### **Advanced Analysis**
The advanced notebook builds on the basic analysis to include:
- Prediction of calories burned using Linear Regression and Random Forest models.
- Clustering analysis to group cycling sessions based on metrics like distance, heart rate, and speed.
- Advanced visualizations comparing actual and predicted calorie values.
- Residual and cluster analysis to gain deeper insights into performance trends.

---

## **Dependencies Required**

The following Python libraries are required to run the notebooks:
- **Core Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical computations.
  - `matplotlib`: For visualizations.
  - `seaborn`: For statistical data visualization.
- **Machine Learning and Clustering**:
  - `scikit-learn`: For regression and clustering models.
  - `scipy`: For additional scientific computing tasks.

Ensure you have Python 3.7 or higher installed. Install the dependencies using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

---

## **Steps to Run the Analyses**

1. **Access the Project Repository**  
   Navigate to the main project repository on GitHub:  
   [Redback Fit Sports Performance Repository](https://github.com/Redback-Operations/redback-fit-sports-performance)

2. **Download Notebooks**  
   - Go to the [Cycling Analysis Notebooks Directory](https://github.com/Redback-Operations/redback-fit-sports-performance/tree/main/Cycling%20Analysis)  
     Download the following files:
     - `Cycling_Basic_Analysis_T3_2024.ipynb`
     - `Cycling_Advanced_Analysis_T3_2024.ipynb`

3. **Download Dataset**  
   - Download the cycling dataset from:  
     [Cycling Data - extended_activities.csv](https://github.com/Redback-Operations/redback-fit-sports-performance/blob/main/Cycling%20Analysis/data/extended_activities.csv)

4. **Open Notebooks**  
   - Open the downloaded notebooks in your preferred environment. The recommended platform is **Google Colab**, but you can also use **Jupyter Notebook** via **Anaconda**.

5. **Load the Dataset**  
   - You can either:
     - Download the dataset and upload it to Google Colab.
     - Use the dataset URL directly in the notebooks to load the data.

6. **Run the Analysis**  
   - Execute each cell in the notebooks sequentially to perform the analyses and generate outputs. The markdown cells in the notebooks include detailed explanations of the steps.



