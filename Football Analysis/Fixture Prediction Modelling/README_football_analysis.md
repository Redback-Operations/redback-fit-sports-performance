# Football Match Analysis Notebook

This directory contains a Jupyter notebook dedicated to analyzing football match data from the `2022-23data.csv` dataset. The notebook performs both classification (predicting match outcomes: Home win, Draw, Away win) and regression (predicting total goals scored) using feature engineering, cross-validation, and machine learning techniques.

---

## **Introduction**

The **Football Match Analysis** notebook is designed to analyze football match data, providing insights into match outcomes and goal-scoring patterns. It leverages metrics such as team rankings, shots, shots on target, fouls, and derived features like total goals, goal difference, and total shots. The notebook includes exploratory data analysis (EDA), classification models to predict match results, and regression models to predict total goals, along with visualizations to interpret results.

Key objectives:
- To preprocess and engineer features from the football dataset.
- To predict match outcomes (Home/Draw/Away) using classification models.
- To predict totalgoals scored using regression models.
- To visualize feature correlations, distributions, and model performance.

---

## **Purpose of the Notebook**

The notebook performs the following tasks:
- **Data Cleaning and Preprocessing**: Handles missing values, parses dates, and ensures data consistency.
- **Feature Engineering**:
  - Creates features like `TotalGoals`, `GoalDiff`, `TotalShots`, `TotalShotsOnTarget`, and `Month` (seasonality).
  - Encodes categorical target (`FTR`) for classification.
- **Exploratory Data Analysis (EDA)**:
  - Generates descriptive statistics for numeric features.
  - Visualizes feature correlations, distributions of engineered features, and seasonal trends in total goals.
- **Predictive Modeling**:
  - **Classification**: Predicts match outcomes (Home/Draw/Away) using Logistic Regression, Random Forest, and Gradient Boosting classifiers.
  - **Regression**: Predicts total goals using Linear Regression, Polynomial Regression, SVR, Random Forest, and Gradient Boosting regressors.
  - Evaluates models using 5-fold cross-validation (accuracy and F1 for classification; RMSE and R² for regression).
- **Visualization**:
  - Plots feature correlations, distributions, seasonal trends, model performance (accuracy, RMSE, R²), confusion matrices, and feature importance for Random Forest models.
  - Generates scatter plots of predicted vs. actual total goals for regression models.

---

## **Dependencies Required**

Ensure the following Python libraries are installed in your environment:
- **Core Libraries**:
  - `pandas`: For data manipulation and analysis.
  - `numpy`: For numerical operations.
  - `matplotlib`: For creating static visualizations.
  - `seaborn`: For advanced statistical visualizations.
  - `pathlib`: For file path handling.
- **Machine Learning**:
  - `scikit-learn`: For classification and regression models, cross-validation, preprocessing, and evaluation metrics.

Install the dependencies using:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## **Steps to Run the Analysis**

1. **Access the Dataset**  
   Ensure the dataset file `2022-23data.csv` is available. Update the file path in the notebook if necessary.

2. **Download the Notebook**  
   Obtain the Jupyter notebook `Football_Analysis.ipynb` from the project directory or repository.

3. **Openweapon: System: Open the Notebook**  
   Open the notebook in your preferred environment. Recommended platforms include:
   - **Google Colab** (upload the notebook and dataset).
   - **Jupyter Notebook** (via Anaconda or other local environments).

4. **Load the Dataset**  
   - Update the `csv_path` variable in the notebook to point to `2022-23data.csv`.
   - Alternatively, upload the dataset to Google Colab or use a direct URL if available.

5. **Run the Analysis**  
   - Execute the notebook cell by cell. Each cell includes comments explaining the preprocessing, EDA, modeling, or visualization steps.
   - Review the outputs, including descriptive statistics, visualizations, and model performance metrics.

---

## **Notebook Structure**

1. **Data Loading and Inspection**:
   - Loads the `2022-23data.csv` dataset and prints its shape, columns, and a preview.
   - ChecksILayout: System: for the existence of the dataset file.

2. **Data Cleaning and Parsing**:
   - Parses the `Date` column (if present) into a datetime format.
   - Removes rows with missing `FTR` (Full-Time Result) values.
   - Fills missing values in numeric columns with 0.

3. **Feature Engineering**:
   - Creates features: `TotalGoals` (FTHG + FTAG), `GoalDiff` (FTHG - FTAG), `TotalShots` (HS + AS), `TotalShotsOnTarget` (HST + AST), and `Month` (from Date).
   - Encodes `FTR` (H/D/A) into numeric labels (H=0, D=1, A=2).

4. **Exploratory Data Analysis (EDA)**:
   - Displays descriptive statistics for numeric features.
   - Plots a correlation heatmap for numeric features.
   - Visualizes distributions of engineered features (`TotalGoals`, `GoalDiff`, `TotalShots`, `TotalShotsOnTarget`).
   - Plots seasonal trends (average total goals by month, if `Date` is present).

5. **Feature Sets and Train/Test Split**:
   - Defines numeric features for classification and regression.
   - Splits data into 80% training and 20% test sets (stratified for classification).

6. **Predictive Modeling**:
   - **Classification Models**:
     - Logistic Regression (`max_iter=2000`).
     - Random Forest Classifier (`n_estimators=300`).
     - Gradient Boosting Classifier.
     - Evaluates using 5-fold cross-validation (accuracy and weighted F1 scores).
   - **Regression Models**:
     - Linear Regression.
     - Polynomial Regression (degree 2).
     - Support Vector Regression (SVR, RBF kernel, `C=2.0`, `epsilon=0.2`).
     - Random Forest Regressor (`n_estimators=300`).
     - Gradient Boosting Regressor.
     - Evaluates using 5-fold cross-validation (RMSE and R² scores).

7. **Evaluation and Visualization**:
   - **Classification**:
     - Prints accuracy, weighted F1, and classification report for the final Random Forest model.
     - Plots a confusion matrix heatmap.
     - Plots feature importance for the Random Forest classifier.
   - **Regression**:
     - Prints MAE, RMSE, and R² for each regression model on the test set.
     - Plots predicted vs. actual total goals for each regression model.
     - Plots feature importance for the Random Forest regressor.
   - Visualizes cross-validation results (accuracy for classification, RMSE and R² for regression) using bar plots.

---

## **Expected Outputs**

- **Descriptive Statistics**: Summary statistics for numeric features.
- **Visualizations**:
  - Correlation heatmap for numeric features.
  - Histograms for engineered features (`TotalGoals`, `GoalDiff`, `TotalShots`, `TotalShotsOnTarget`).
  - Seasonal trend plot (average total goals by month, if applicable).
  - Bar plots for classification (accuracy) and regression (RMSE, R²) cross-validation results.
  - Confusion matrix heatmap for classification.
  - Scatter plots of predicted vs. actual total goals for regression models.
  - Feature importance bar plots for Random Forest models (classification and regression).

- **Model Performance**:
  - **Classification**: Cross-validation accuracy and weighted F1 scores, test set accuracy, F1, and classification report.
  - **Regression**: Cross-validation RMSE and R² scores, test set MAE, RMSE, and R² scores.

---

## **Notes**

- Ensure the dataset path is correctly specified to avoid file-loading errors.
- The notebook assumes the dataset contains columns like `FTR`, `FTHG`, `FTAG`, `HS`, `AS`, `HST`, `AST`, `HF`, `AF`, `H_Ranking_Prior_Season`, `A_Ranking_Prior_Season`, and optionally `Date`. Verify the column names match your dataset.
- For improved performance, consider tuning hyperparameters for Random Forest or Gradient Boosting models (e.g., adjusting `n_estimators`, `max_depth`, or learning rate).
- The Random Forest models use 300 trees by default; increasing this number may improve accuracy but will increase computation time.
- The SVR regression model uses specific hyperparameters (`C=2.0`, `epsilon=0.2`); these can be tuned for better performance if needed.