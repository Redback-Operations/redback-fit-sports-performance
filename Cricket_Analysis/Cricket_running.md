# Virat Kohli Cricket Batting Analysis and Prediction

This Jupyter notebook performs an exploratory data analysis (EDA) and predictive modeling on Virat Kohli's cricket batting performance data. The dataset includes metrics like runs scored, balls faced (BF), strike rate (SR), boundaries (4s and 6s), opposition, ground, and start date. It uses machine learning to predict runs based on key features and provides insights into Kohli's performance.

## Overview
- **Dataset**: "Data player virat.csv" (Virat Kohli's ODI/T20I innings data, ~106 rows).
- **Key Sections**:
  1. **Load & Clean Dataset**: Loads the CSV, skips header rows, converts numeric columns (Runs, BF, SR, 4s, 6s), and parses dates.
  2. **Summary Statistics**: Displays descriptive stats for numeric columns and a histogram (via Matplotlib).
  3. **Predictive Modeling**: Trains Linear Regression and Random Forest models to predict "Runs" using features [BF, SR, 4s, 6s]. Evaluates with R², MAE, and RMSE. Plots feature importance.
  4. **Insights**: Highlights max/avg runs, best opposition (e.g., vs Afghanistan), and model takeaways.
- **Libraries Used**: pandas, numpy, matplotlib, seaborn, scikit-learn (train_test_split, LinearRegression, RandomForestRegressor, metrics).
- **Outputs**:
  - Cleaned DataFrame head.
  - Summary stats table.
  - Model evaluation metrics (e.g., Random Forest R² ~0.85, depending on split).
  - Bar plot of feature importance (SR and 6s often most important).
  - Insights: Highest score 122, avg 37.57 runs; boundaries drive predictions.

## Requirements
- Python 3.12+ (tested with 3.13.5).
- Install dependencies:


```python

```
