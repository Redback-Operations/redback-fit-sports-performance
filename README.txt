# ReflexionPro Predictive Modeling

## Overview
This project builds a **predictive model** to estimate running duration based on activity data collected from wearable devices. The model leverages stacked ensemble learning, combining multiple regression models to improve accuracy and generalisation.

This work is part of my Capstone Project with **Redback Operations – ReflexionPro**, focusing on applying data science and machine learning to athlete performance analytics.

## Dataset
- The dataset used is activities_cleaned.csv, containing 155 recorded running activities with features such as:
- Distance (Raw) – total distance covered (meters)
- Elevation Gain (Raw) – elevation gain during the run (meters)
- Average Moving Speed – pace data (converted to seconds per km)
- Duration (h:m:s) – run duration (converted to seconds for modelling)
- Environmental conditions: temperature, humidity, wind speed

## Features
- Data Preprocessing
  - Converted duration (h:m:s → seconds)
  - Converted pace (min:sec/km → seconds per km)
  - Cleaned and filtered dataset for valid entries
- Models Trained
  - Linear Regression
  - Ridge Regression
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - XGBoost Regressor
  - CatBoost Regressor
- Stacking Ensemble
  - Combines all base models with a Linear Regression meta-learner
- Predictive modeling of running and cycling activity duration using features such as distance, pace, and elevation gain.
- Implementation of **advanced boosting models**:  
  - XGBoost  
  - CatBoost  
- Application of **k-fold cross-validation** for robust model evaluation.  
- **Hyperparameter tuning** with `GridSearchCV` and `RandomizedSearchCV` for optimal performance.  
- Data visualisation of actual vs predicted durations for interpretability.  

## Methods
- Stacking ensemble method combining multiple base learners.  
- Boosting algorithms for improved predictive accuracy.  
- Performance evaluation using metrics such as RMSE, MAE, and R².  

## Results
- Evaluation Metrics
  - RMSE (Root Mean Squared Error) on test set
  - R² Score (goodness of fit)
  - 5-Fold Cross-Validation RMSE
- Visualisation
  - Actual vs Predicted Running Duration scatter plot

## Requirements
- Python 3.8+
- Libraries: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `catboost`, `matplotlib`, `plotly`

Install dependencies:
```bash
pip install -r requirements.txt

## How to Run
- Clone this repository:
git clone https://github.com/Redback-Operations/redback-fit-web.git
cd repository-name(redback-fit-sports-performance)

- Install dependencies:
pip install -r requirements.txt

- Run the Jupyter Notebook or Python script:
jupyter notebook Running_Duration.ipynb

## Author
Hrithik Joseph Narlely
Data Science – Redback Operations (Project 3: ReflexionPro)
