# 20km Free Trial Cycling Analysis Notebook

This directory contains a Jupyter notebook dedicated to analyzing cycling performance data from a 20km free trial: **20kmfreetrialCycling.ipynb**. This notebook aims to explore, analyze, and model insights from cycling trials under different conditions. The notebook utilizes the `20kmfreetrial.csv` dataset.

---

## **Introduction**

The 20km free trial cycling analysis notebook is part of the athlete performance analysis project, focusing on uncovering patterns and trends in cycling data from controlled trials. By analyzing metrics like power output, cadence, heart rate (HR), peak power output (PPO), and relative power, this notebook provides insights into performance variations across conditions and trials. It includes data exploration, visualization, and predictive modeling to compare different machine learning approaches.

Key objectives of this notebook:
- To load, clean, and preprocess cycling trial data.
- To generate descriptive statistics and visualizations for key performance metrics.
- To examine relationships between variables like power, cadence, HR, and conditions.
- To build and compare predictive models for metrics such as power output.
- To facilitate data-driven decisions for understanding cycling performance in trial settings.

---

## **Purpose of the Notebook**

### **20km Free Trial Cycling Analysis**
This notebook provides a comprehensive analysis of cycling data:
- Data loading from CSV and initial exploration (e.g., dataset shape, first rows, column types, summary statistics).
- Handling missing values and deriving any necessary features.
- Visualizing distributions (histograms), correlations (heatmaps), and comparisons (boxplots by condition/trial).
- Applying machine learning techniques to predict targets like 'Power' using features such as 'Cadence', 'HR', 'Condition', etc.
- Comparing models including Linear Regression, Random Forest, Gradient Boosting, and XGBoost using K-Fold Cross Validation for R² and RMSE metrics.
- Visualizing model performance comparisons with bar plots.

---

## **Dependencies Required**

Ensure that the following Python libraries are installed in your environment:
- **Core Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical operations.
  - `matplotlib`: For creating static visualizations.
  - `seaborn`: For advanced statistical visualizations.
- **Machine Learning**:
  - `scikit-learn`: For regression models, cross-validation, and metrics.
  - `xgboost`: For the XGBoost regressor model.

Install the dependencies using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost

## **Steps to Run the Analysis**

1. **Access the Project Repository**  
   Navigate to the main project repository on GitHub:  
   [Redback Fit Sports Performance Repository](https://github.com/Redback-Operations/redback-fit-sports-performance)

2. **Download Notebook**  
   - Go to the relevant directory in the repository.  
   - Download the following file:  
     - `20kmfreetrialCycling.ipynb`

3. **Download Dataset**  
   - Download the cycling dataset from the repository or relevant source:  
     `20kmfreetrial.csv`  
     (Note: Ensure the dataset is placed in the same directory as the notebook or adjust the file path in the code.)

4. **Open Notebook**  
   - Open the downloaded notebook in your preferred environment. The most recommended platform is **Google Colab**, but you can also use **Jupyter Notebook** via **Anaconda**.

5. **Load the Dataset**  
   - You can either:  
     - Download the dataset locally and upload it to Google Colab.  
     - Use a direct file path in the notebook to load the data.

6. **Run the Analysis**  
   - Execute the notebook cell by cell. Each cell contains comments and explanations to guide you through the analysis process.  
   - Review outputs, visualizations, model comparison results, and insights.


```python

```
