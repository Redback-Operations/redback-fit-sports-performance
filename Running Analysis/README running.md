# Running Analysis (Basic and Advanced)

This directory contains two Jupyter notebooks dedicated to analyzing running performance data: **Basic Analysis** and **Advanced Analysis**. These notebooks aim to explore, analyze, and extract insights from the athlete's running activities. Both notebooks utilize the `Fixed_cleaned_activities.csv` dataset, which is available in the project repository.

---

## **Introduction**

The running analysis notebooks are part of the athlete performance analysis project, focusing on uncovering patterns and trends in running data. By analyzing metrics like distance, speed, heart rate, and calories burned, these notebooks provide insights into the athlete's training regimen and physiological responses. They also include advanced techniques to predict key metrics, identify relationships between variables, and visualize training progress over time.

Key objectives of these notebooks:
- To understand and visualize basic trends in running performance metrics.
- To apply advanced statistical and machine learning techniques for deeper insights.
- To facilitate data-driven decisions for improving training and performance.

---

## **Purpose of the Notebooks**

### **Basic Analysis**
This notebook serves as an entry point for understanding the dataset and exploring its characteristics:
- Data cleaning and preprocessing to filter relevant metrics.
- Generating descriptive statistics for key variables.
- Visualizing trends over time for metrics such as distance, speed, heart rate, and calories.
- Examining relationships between metrics using scatter plots and correlation matrices.

### **Advanced Analysis**
This notebook extends the basic analysis with sophisticated methodologies:
- Regression analysis to predict calories burned based on distance, speed, and heart rate.
- Clustering analysis to identify patterns in running sessions and group similar activities.
- Time series forecasting using Prophet to predict future trends in distance and speed.
- Machine learning techniques, including Random Forest and Support Vector Regression, for advanced predictive modeling.

---

## **Dependencies Required**

Ensure that the following Python libraries are installed in your environment:
- **Core Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical operations.
  - `matplotlib`: For creating static visualizations.
  - `seaborn`: For advanced statistical visualizations.
- **Machine Learning and Forecasting**:
  - `scikit-learn`: For regression and clustering models.
  - `prophet`: For time-series forecasting.
  - `scipy`: For additional scientific computing support.

Install the dependencies using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn prophet
```

---

## **Steps to Run the Analyses**

1. **Access the Project Repository**  
   Navigate to the main project repository on GitHub:  
   [Redback Fit Sports Performance Repository](https://github.com/Redback-Operations/redback-fit-sports-performance)

2. **Download Notebooks**
   - Go to the [Running Analysis Notebooks Directory](https://github.com/Redback-Operations/redback-fit-sports-performance/tree/main/Running%20Analysis).  
     Download the following files:
     - `Running_Basic_analysis_T3_2024.ipynb`
     - `Running_Advanced_Analyis_T3_2024.ipynb`

3. **Download Dataset**
   - Download the running dataset from:  
     [Running Data - Fixed_cleaned_activities.csv](https://github.com/Redback-Operations/redback-fit-sports-performance/blob/main/Running_Archive/Fixed_cleaned_activities.csv)

4. **Open Notebooks**
   - Open the downloaded notebooks in your preferred environment. The most recommended platform is **Google Colab**, but you can also use **Jupyter Notebook** via **Anaconda**.

5. **Load the Dataset**
   - You can either:
     - Download the dataset locally and upload it to Google Colab.
     - Use the dataset URL directly in the notebooks to load the data.

6. **Run the Analysis**
   - Execute the notebooks cell by cell. Each cell contains comments and explanations to guide you through the analysis process.
   - Review outputs, visualizations, and model evaluations to extract insights.

---

