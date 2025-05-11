# Recovery Time Estimator

## Introduction

The objective of this project is to develop a reproducible, end-to-end pipeline that transforms raw wearable data into a quantitative estimate of physiological recovery. Leveraging publicly available Fitbit exercise and sleep logs, the pipeline employs a three-layer Medallion architecture—raw (raw ingestion), processed (data cleaning and harmonization), and curated (feature curation)—to derive a continuous “recovery hours” metric for each user on a daily basis. The resulting framework not only facilitates rigorous academic evaluation of model performance but also establishes a foundation for future deployment in personalized health applications.

---

## Repository Contents

- **1.DataPreProcessor/**  
  Scripts responsible for loading raw JSON exports, filtering out noise and aligning timestamps.

- **2.FeatureEngineering/**  
  Code modules that merge and aggregate cleaned exercise and sleep records into a unified, per-user daily feature table suitable for modeling.

- **3.ModelSelectionAndTraining/**  
  Computes an initial proxy for recovery and Experimental workflows evaluating multiple regression algorithms, conducting hyperparameter optimization, and performing cross-validation to identify the optimal predictive model.

- **4.TestingAndDeployment/** 
  Collects exercise and sleep metrics from the user, standardizes the inputs, and uses a pre-trained model to predict recovery time. It then categorizes the prediction as faster, average, or slower recovery based on predefined thresholds, running in a continuous loop until the user exits.


- **data/**  
  - `raw/` Bronze layer: original Fitbit JSON exports.  
  - `processed/` Silver layer: cleaned and standardized logs.  
  - `curated/`  Gold layer: final feature matrices and recovery labels.  

- **requirements.txt**  
  A version-pinned list of Python dependencies to ensure reproducibility.

---

## Achievements To Date

1. **Data Ingestion and Cleaning**  
   • Raw exercise and sleep data successfully ingested and processed to remove anomalies, missing values, and timestamp inconsistencies.  

2. **Feature Derivation**  
   • Key predictors—including aggregated step counts, heart-rate summaries, sleep efficiency metrics, and workout load—have been computed and consolidated into a single, analysis-ready dataset.  

3. **Proxy Recovery Metric**  
   • A continuous recovery hours label was defined, validated, and smoothed via a rolling window to reflect realistic physiological adaptation.  

4. **Model Evaluation**  
   • Multiple regression models (linear regression, decision trees, random forests, support vector regression, and gradient boosting) were benchmarked.  
   • Support vector regression was selected as the best performer based on mean absolute error, root mean squared error, and coefficient of determination.

5. **Testing and Deployment Preparation**  
   • The prediction logic was tested with standardized inputs to verify consistency with the training distribution.  
   • Model loading, data preprocessing, and real-time inference were packaged for seamless deployment to backend APIs.  
   • The script was optimized for command-line and API integration, ensuring efficient data handling and quick response times. 

---

## Future Work

- This code represents a foundational framework aimed at developing an end-to-end recovery time estimation pipeline from a data science perspective. It covers the entire process, starting from data collection through a medallion architecture, followed by data preprocessing, model selection, testing, and deployment-ready code. Throughout this process, several proxy variables were used to achieve the desired results. 

- However, there is significant potential for improvement across all stages of the pipeline, from refining data preprocessing techniques to optimizing the model selection process. Each component—from data handling to model performance—can be enhanced or modified to achieve more accurate and reliable results. This is just the beginning, and further iterations will be essential for refining the system and reaching its full potential in real-world applications.

---
