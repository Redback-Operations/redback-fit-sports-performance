# VO2 Max Prediction from Running Activities (ML Pipeline)

This Jupyter notebook implements a full machine learning pipeline to predict VO2 Max from running activity data. It includes data loading, EDA, preprocessing, model training (Linear Regression, Random Forest, SVR), cross-validation, evaluation, and visualizations. The focus is on predicting aerobic fitness (VO2 Max) using features like distance, heart rates, speed, power, and more.

## Overview
- **Dataset**: "simu_vo2_activities.csv" (345 rows, 44 columns of running metrics).
- **Key Sections**:
  1. **Load & Prep**: Loads CSV, selects target "VO2 Max", handles missing values, prints summary and columns.
  2. **EDA**: Numeric summaries, histograms for first 10 features, correlation heatmap (top 10 features).
  3. **Feature Engineering & Preprocessing**: Selects numeric/categorical features, uses ColumnTransformer (StandardScaler + OneHotEncoder).
  4. **Modeling**: Trains pipelines for LinearRegression, RandomForest (100 estimators), SVR (RBF kernel). 5-fold CV with R², RMSE, MAE.
  5. **Evaluation**: Best model (usually Random Forest, R² ~0.90+), actual vs. predicted scatter, residuals histogram, feature importance (top 15), seasonal trend plot.
  6. **Predictions**: Adds predicted/residual columns; prints sample for first 10 rows.
- **Libraries Used**: pandas, numpy, matplotlib, seaborn, scikit-learn (Pipeline, ColumnTransformer, StandardScaler, OneHotEncoder, models, cross_val_score/predict, metrics, KFold).
- **Outputs**:
  - Dataset shape/columns/summary.
  - Histograms and correlation heatmap.
  - CV results table (e.g., Random Forest R² mean 0.92, RMSE ~1.5).
  - Plots: Actual vs Predicted, residuals, feature importance (e.g., Avg Watts, Distance top), monthly trend.
  - Sample predictions table.

## Requirements
- Python 3.12+ (tested with 3.13.5).
- Install dependencies:


```python

```
