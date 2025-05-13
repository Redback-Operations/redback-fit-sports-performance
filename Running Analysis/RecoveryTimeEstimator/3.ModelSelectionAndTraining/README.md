# Model Selection and Training

This captures a complete workflow for transforming raw exercise and sleep data that we created in `FeatureEngineering` into a robust recovery-time predictor:

1. **StandardizingAndProxyRecoveryTimeCalculation.ipynb**
As we do not have the recovery time recorder, we try to calculate a proxy recovery time using the available variables (*In the future, if the recovery time is available, this file needs to be altered*)
   - Imputes missing values using column-wise medians  
   - Normalizes each metric per user (z-score) to remove inter-user scale differences  
   - Builds a composite recovery score (sleep score minus training load)  
   - Converts the score to a bounded “recovery hours” measure via percentile-based scaling  
   - Smooths daily estimates with a 7-day rolling average  
   - Outputs the curated dataset: **recovery_time_ready_for_model.csv**

2. **ModelSelectionAndTraining.ipynb**  
   - Loads the preprocessed `recovery_time_ready_for_model.csv`  
   - Splits every user’s timeline into 70% train, 15% validation, 15% test  
   - Employs GroupKFold cross-validation to tune and compare:  
     - Baseline mean predictor  
     - Linear Regression  
     - KNN Regressor  
     - Decision Tree  
     - Random Forest  
     - Gradient Boosting  
     - Support Vector Regression (SVR)  
   - Selects SVR as the top performer on Test MAE  
   - Persists the final model as **svr_model.pkl**

3. **Supporting Files**  
   - **recovery_time_ready_for_model.csv** — ready-to-train feature set  
   - **svr_model.pkl** — serialized best model for inference  
