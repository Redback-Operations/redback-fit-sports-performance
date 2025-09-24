# Muscle Activation – Chiranth’s Contribution

This section contains my work on **Muscle Activation analysis** as part of the Redback Fit Sports Performance project.  
The goal is to process and analyze EMG (Electromyography) signals from strength training sessions, build predictive models, and generate reports that can guide athlete performance and recovery.

---

## Folder Overview

###  DATA
- **SEMG_DB12/** → Raw and cleaned EMG datasets used for analysis.

###  notebooks
- **reflectionpro-update-1.ipynb / -2.ipynb / -3.ipynb** → Iterative development notebooks showing data cleaning, feature extraction, and model building.  
- **reflectionpro.ipynb** → Consolidated analysis notebook.  
- **serve_lean_api.py** → API script for serving model predictions.  

###  models
- **multi_muscle_rf.joblib** → Saved Random Forest model.  
- **multi_muscle_rf_lean.joblib** → Optimized/lean version of the model.  

###  plots & reports
- **athlete_report_*.png** → Per-muscle reports (RF, BF, ST, VM) showing activation patterns.  
- **fatigue_session_summary.csv** → Summaries of fatigue analysis across sessions.  
- **loso_per_subject.csv / loso_r2_by_subject_*.png** → Leave-One-Subject-Out validation results.  
- **multi_muscle_window_predictions.csv / per_rep_predictions.json** → Prediction outputs.  
- **ablation_results.csv** → Results from feature ablation testing.  
- Combined set of figures and CSVs for visualizing and validating outcomes.

---

## Key Contributions

- **Data Cleaning & Processing**  
  - Standardized raw SEMG data into structured CSVs.  
  - Handled inconsistent formats and ensured reproducibility.  

- **Feature Engineering & Modeling**  
  - Extracted features (RMS, variance, windowed summaries).  
  - Trained Random Forest models for multi-muscle prediction.  
  - Exported trained models (`.joblib`) for reuse in the pipeline.  

- **Analysis & Reporting**  
  - Built visual reports of muscle activation across multiple subjects.  
  - Evaluated performance with **Leave-One-Subject-Out (LOSO)** validation.  
  - Generated athlete-specific and fatigue summaries.  

- **Deployment Work**  
  - Drafted a Python API (`serve_lean_api.py`) to serve predictions.  

---

## How to Use

1. **Set up environment**  
   Install Python 3 and required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Explore data**  
   Open any notebook in `notebooks/` to view the full pipeline:
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

3. **Run model predictions**  
   Load the saved models from `models/` in Python:
   ```python
   import joblib
   model = joblib.load("models/multi_muscle_rf.joblib")
   predictions = model.predict(X_test)
   ```

4. **View reports**  
   Navigate to `plots & reports/` for PNG figures and CSV summaries.

---

## Outcomes & Next Steps

- Cleaned and structured SEMG dataset for analysis.  
- Developed and saved predictive Random Forest models.  
- Produced athlete-specific activation and fatigue reports.  
- Drafted API for integration with team dashboard.  

**Next Steps:**  
- Expand model evaluation with more feature sets.  
- Integrate API into team’s performance monitoring dashboard.  
- Collaborate with teammates to connect model outputs to visualization front-end.  

---

**Maintainer:** Chiranth Gowda Mahesh Kumar  
**Location:** `Muscle Activation/Chiranth/`
