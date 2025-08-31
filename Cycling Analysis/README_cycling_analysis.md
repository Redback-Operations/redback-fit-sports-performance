# Cycling Analysis Notebook

This directory contains a Jupyter notebook dedicated to analyzing cycling performance data using the `extended_activities_with_ftp.csv` dataset. The notebook focuses on exploring and predicting calorie expenditure during cycling activities through feature engineering and machine learning techniques.

---

## **Introduction**

The **Cycling Analysis** notebook is designed to analyze cycling performance data, providing insights into an athlete's training through exploratory data analysis (EDA) and predictive modeling. By leveraging metrics such as distance, average power (watts), speed, elevation gain, and derived features like speed-to-power ratio and altitude gain per kilometer, the notebook aims to predict calories burned and evaluate model performance.

Key objectives:
- To preprocess and engineer features from the cycling dataset.
- To evaluate multiple regression models for predicting calorie expenditure.
- To visualize model predictions and compare their accuracy.

---

## **Purpose of the Notebook**

The notebook performs the following tasks:
- **Feature Engineering**: Creates derived features such as `speed_to_power_ratio` and `altitude_gain_per_km` to enhance model performance.
- **Data Preprocessing**: Handles missing values using mean imputation and splits data into training and test sets.
- **Predictive Modeling**:
  - Implements four regression models: Linear Regression, Polynomial Regression (degree 2), Support Vector Regression (SVR), and Random Forest Regression.
  - Evaluates models using 5-fold cross-validation and R² scores on the test set.
- **Visualization**:
  - Generates scatter plots of predicted vs. actual calories for each model.
  - Produces a bar chart comparing R² scores across models.

---

## **Dependencies Required**

Ensure the following Python libraries are installed in your environment:
- **Core Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical operations.
  - `matplotlib`: For creating static visualizations.
  - `seaborn`: For advanced statistical visualizations.
- **Machine Learning**:
  - `scikit-learn`: For regression models, cross-validation, preprocessing, and evaluation metrics.

Install the dependencies using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## **Steps to Run the Analysis**

1. **Access the Dataset**  
   Ensure the dataset file `extended_activities_with_ftp.csv` is available. Update the file path in the notebook if necessary.

2. **Download the Notebook**  
   Obtain the Jupyter notebook `Cycling_Analysis.ipynb` from the project directory or repository.

3. **Open the Notebook**  
   Open the notebook in your preferred environment. Recommended platforms include:
   - **Google Colab** (upload the notebook and dataset).
   - **Jupyter Notebook** (via Anaconda or other local environments).

4. **Load the Dataset**  
   - Update the file path in the notebook to point to `extended_activities_with_ftp.csv`.
   - Alternatively, upload the dataset to Google Colab or use a direct URL if available.

5. **Run the Analysis**  
   - Execute the notebook cell by cell. Each cell includes comments explaining the preprocessing, modeling, or visualization steps.
   - Review the outputs, including cross-validation scores, test R² scores, and visualizations.

---

## **Notebook Structure**

1. **Data Loading and Feature Engineering**:
   - Loads the dataset `extended_activities_with_ftp.csv`.
   - Creates new features:
     - `speed_to_power_ratio`: Average speed divided by average watts (with a small constant to avoid division by zero).
     - `altitude_gain_per_km`: Elevation gain divided by distance (with a small constant to avoid division by zero).

2. **Data Preprocessing**:
   - Defines features (`Distance`, `Average Watts`, `Average Speed`, `Elevation Gain`, `speed_to_power_ratio`, `altitude_gain_per_km`) and target (`Calories`).
   - Handles missing values using mean imputation.
   - Splits data into 80% training and 20% test sets with a fixed random state.

3. **Predictive Modeling**:
   - Implements four models:
     - **Linear Regression**: A baseline linear model.
     - **Polynomial Regression (degree 2)**: Extends linear regression with polynomial features and standard scaling.
     - **Support Vector Regression (SVR)**: Uses an RBF kernel with tuned hyperparameters (`C=100`, `gamma=0.1`, `epsilon=0.1`).
     - **Random Forest Regression**: Uses 100 trees with a fixed random state.
   - Evaluates models using 5-fold cross-validation (R² scores) on the training set and computes test R² scores.

4. **Visualization**:
   - Scatter plots of predicted vs. actual calories for each model, with a red dashed line for reference.
   - Bar chart comparing R² scores across all models, with values ranging from 0 to 1.

---

## **Expected Outputs**

- **Model Performance**:
  - Cross-validation R² scores for each model (printed for each fold).
  - Test R² scores for each model, indicating predictive accuracy on unseen data.

- **Visualizations**:
  - Four scatter plots (one per model) showing predicted vs. actual calories.
  - A bar chart comparing R² scores across models.

---

## **Notes**

- Ensure the dataset path is correctly specified to avoid file-loading errors.
- The notebook assumes the dataset contains columns like `Distance`, `Average Watts`, `Average Speed`, `Elevation Gain`, and `Calories`. Verify the column names match your dataset.
- For improved model performance, consider experimenting with hyperparameter tuning for SVR (e.g., adjusting `C`, `gamma`, or `epsilon`) or Random Forest (e.g., increasing `n_estimators` or tuning `max_depth`).
- The Random Forest model uses 100 trees by default; increasing the number of trees may improve accuracy but will increase computation time.