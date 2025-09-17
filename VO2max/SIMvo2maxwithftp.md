# ReflexionPro – VO₂ Max and FTP Modeling

##  Project Overview
This project is part of my Capstone with **Redback Technologies**, where I contributed as a Data Analysis team member.  
The main objective was to analyze wearable performance data and build predictive models that link **VO₂ Max** (aerobic capacity) with **Estimated FTP** (Functional Threshold Power).  
The insights aim to improve **ReflexionPro**, a platform providing personalized training recommendations for athletes.

---

##  Dataset
- File: `simu_vo2_activities_with_ftp.csv`  
- Key Columns Used:
  - **VO2 Max** – target variable (ml/kg/min)  
  - **Estimated_FTP** – predictor variable (Watts)  
- Preprocessing:
  - Removed missing values and outliers  
  - Converted data to numeric types for consistency  

---

##  Methods
The following models were implemented and compared:

1. **Linear Regression** – baseline model for simple trends  
2. **Polynomial Regression** (degree 2 & 3) – captures non-linear patterns  
3. **Support Vector Regression (SVR)** – tested with linear and RBF kernels  
4. **Random Forest Regression** – ensemble model for complex relationships  

Each model was evaluated with **5-Fold Cross Validation**, using:
- **R² Score** (higher = better fit)  
- **RMSE** (lower = fewer errors)  

---

##  Results
- Random Forest delivered the best predictive accuracy, handling non-linearity and noise effectively.  
- Polynomial and SVR models performed moderately well.  
- Linear Regression provided a clear but limited baseline.  
- A ranking bar chart (R² scores) was created to visualize best-to-worst models.  

---

##  How to Run
1. Open the Jupyter notebook: `simvo2activitieswithftp.ipynb`  
2. Install required libraries if missing:  
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn



```python

```
