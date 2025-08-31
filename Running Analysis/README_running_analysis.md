# Running Analysis Notebooks

This directory contains a Jupyter notebook dedicated to analyzing running performance data: **Running Analysis**. The notebook aims to explore, analyze, and extract insights from an athlete's running activities using the `activities_cleaned 1.csv` dataset.

---

## **Introduction**

The **Running Analysis** notebook is part of the athlete performance analysis project, focusing on uncovering patterns and trends in running data. By analyzing metrics such as distance, speed, heart rate, calories burned, and environmental factors like temperature and rainfall, this notebook provides insights into the athlete's training regimen and physiological responses. It includes exploratory data analysis (EDA) and predictive modeling to facilitate data-driven decisions for improving training and performance.

Key objectives:
- To understand and visualize trends in running performance metrics.
- To apply statistical and machine learning techniques for predictive modeling.
- To identify relationships between variables and predict calories burned.

---

## **Purpose of the Notebook**

The **Running Analysis** notebook provides a comprehensive analysis of running data, including:
- **Data Preprocessing**: Cleaning and feature engineering, such as converting pace to speed (km/h), duration to minutes, and handling missing or malformed data.
- **Exploratory Data Analysis (EDA)**:
  - Generating descriptive statistics for key variables.
  - Visualizing distributions of calories, duration, and distance.
  - Examining relationships between metrics using scatter plots and correlation heatmaps.
  - Detecting outliers using boxplots.
- **Predictive Modeling**:
  - Applying multiple regression models (Linear Regression, Polynomial Regression, SVR, Random Forest) to predict calories burned.
  - Evaluating model performance using 5-fold cross-validation with R² scores.
  - Visualizing predicted vs. actual calories for model comparison.

---

## **Dependencies Required**

Ensure the following Python libraries are installed in your environment:
- **Core Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical operations.
  - `matplotlib`: For creating static visualizations.
  - `seaborn`: For advanced statistical visualizations.
- **Machine Learning**:
  - `scikit-learn`: For regression models, cross-validation, and preprocessing.

Install the dependencies using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## **Steps to Run the Analysis**

1. **Access the Dataset**  
   Ensure you have the dataset file `activities_cleaned 1.csv` available. Update the file path in the notebook if necessary.

2. **Download the Notebook**  
   Obtain the Jupyter notebook `Running_Analysis.ipynb` from the project directory or repository.

3. **Open the Notebook**  
   Open the notebook in your preferred environment. Recommended platforms include:
   - **Google Colab** (upload the notebook and dataset).
   - **Jupyter Notebook** (via Anaconda or other local environments).

4. **Load the Dataset**  
   - Update the `path` variable in the notebook to point to `activities_cleaned 1.csv`.
   - Alternatively, upload the dataset to Google Colab or use a direct URL if available.

5. **Run the Analysis**  
   - Execute the notebook cell by cell. Each cell includes comments explaining the preprocessing, EDA, or modeling steps.
   - Review the outputs, including visualizations (e.g., histograms, scatter plots, correlation heatmaps) and model performance metrics (e.g., R² scores).

---

## **Notebook Structure**

1. **Helper Functions**:
   - `pace_to_speed_kmh`: Converts pace (MM:SS per km) to speed (km/h).
   - `hms_to_minutes`: Converts duration (HH:MM:SS) to total minutes.
   - `clean_calories`: Removes commas from calorie values and casts to float.

2. **Data Preprocessing**:
   - Loads the dataset and creates new features (e.g., `avg_speed_kmh`, `duration_min`, `Calories_num`).
   - Handles missing values and categorical variables (e.g., `RainfallBin`).

3. **Exploratory Data Analysis**:
   - Displays dataset shape and summary statistics.
   - Generates distribution plots for calories, duration, and distance.
   - Creates scatter plots to explore relationships between calories and variables like distance, speed, and heart rate.
   - Produces a correlation heatmap and boxplot for outlier detection.

4. **Predictive Modeling**:
   - Defines numeric and categorical features for modeling.
   - Uses a `ColumnTransformer` to preprocess features (imputation, scaling, one-hot encoding).
   - Implements four models: Linear Regression, Polynomial Regression (degree 2), SVR (RBF kernel), and Random Forest.
   - Evaluates models using 5-fold cross-validation and visualizes R² scores.
   - Plots predicted vs. actual calories for each model.

---

## **Expected Outputs**

- **Visualizations**:
  - Histograms of calories, duration, and distance distributions.
  - Scatter plots showing relationships between calories and key metrics.
  - Correlation heatmap for numeric features.
  - Boxplot for outlier detection in calories.
  - Bar chart comparing R² scores of predictive models.
  - Scatter plots of predicted vs. actual calories for each model.

- **Model Performance**:
  - R² scores and standard deviations from 5-fold cross-validation for each model.
  - Insights into which model performs best for predicting calories burned.

---

## **Notes**

- Ensure the dataset path is correctly specified in the notebook to avoid file-loading errors.
- The notebook assumes the dataset contains columns like `Average Speed`, `Duration (h:m:s)`, `Calories`, `Distance (Raw)`, and `Average Heart Rate (bpm)`. Verify the column names match your dataset.
- For advanced users, consider experimenting with hyperparameter tuning for the SVR or Random Forest models to improve performance.