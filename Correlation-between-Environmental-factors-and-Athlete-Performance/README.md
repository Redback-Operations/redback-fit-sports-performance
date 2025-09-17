# Correlate Environmental Factors (Temperature, Wind Speed, Humidity) with Athlete Performance Metrics

## Introduction
This directory contains one Jupyter notebook which used to implement a correlation between environmental factors and athlete performance metrics. I use raw data to perform exploratory data analysis (EDA), preprocess the data, and performs XGBoost Regression modeling to study the relationship between features like elevation gain, elevation loss, average heart rate, aveage speed, moving duration, distance and calories.

## Notebook Contains

- **1.Preprocess the data/**
  - Load the raw data
  - Extract relevant features
  - Handle missing values
  - Filter out extreme outliers (noise)
  
- **2.Correlate environmental factors and athlete's performance/**
  - Perform spearman correlation
  - Visualise the relationship using a heatmap between environmental factors and performance

- **3.XGBoost Regression model/**
  - Perform XGBoost Regressor to identify non-linear relationship in environmental factors with athlete's performance.

## Dependencies Required

Ensure that the following libraries are installed in the environment
- `pandas` : For data manipulation and analysis
- `numpy`: For numerical computations
- `matplotlib`: For data visualisation
- `seaborn`: For advanced statistical visualisation (optional)
- `scikit_learn`: For XGBoost Regression model

## Access to the project Repository
  The main project repository on GitHub :
  [Redback Fit Sports Performance Repository](https://github.com/Redback-Operations/redback-fit-sports-performance)
  
- **Dataset** - The running dataset from:
  [Running Data - activities_cleaned.csv](https://github.com/Redback-Operations/redback-fit-sports-performance/Running_Archive/blob/main/Fixed_cleaned_activities.csv)

- **Open NoteBook**
  Open the downloaded notebooks in Google Colab or Jupyter Notebook via Anaconda
