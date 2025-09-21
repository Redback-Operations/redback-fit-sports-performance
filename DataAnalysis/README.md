## 1. Introduction
This folder contains my personal contributions for the SIT764 Data Analysis Team project.  
The work focuses on cleaning workout datasets, performing exploratory data analysis (EDA),  
building regression models, and visualising relationships between athlete performance metrics and environmental factors.

---

## 2. Code
The Jupyter Notebooks (`.ipynb`) in this directory include the following tasks:

- **Data Cleaning & Visualization**  
  - Converted timestamps, calculated workout duration, removed missing values.  
  - Visualised workout duration by weather condition and distance vs average speed.

- **Outlier Detection**  
  - Identified unrealistic workout durations (>1000 min) using boxplots.  

- **Workout Duration Distribution**  
  - Analysed distribution of workout durations with histograms.  

- **Weather vs Heart Rate**  
  - Explored the effect of weather conditions on average heart rate.  

- **Regression Model**  
  - Built a Linear Regression model to predict workout duration.  

- **Final Model**  
  - Re-validated regression model and summarised results.  

---

## 3. Data
The analysis uses the cleaned dataset provided in `activities_cleaned 1.csv`.  

Key features used include:  
- Distance (km)  
- Calories (kcal)  
- Wind Speed (m/s)  
- Temperature (°C)  
- Workout Duration (minutes)  
- Average Heart Rate (bpm)  

Data was preprocessed to handle missing values and filter unrealistic entries.

---

## 4. Tools
- Python (pandas, numpy, matplotlib, seaborn, scikit-learn)  
- Jupyter Notebook for analysis and visualisation  

---

## 5. Notes
All notebooks include both **code** and **evidence** (plots, tables, metrics).  
This demonstrates a week-by-week progression from **data cleaning → EDA → modelling → final summary**.
