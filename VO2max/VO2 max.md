# VO2 Max Analysis from Running Activities

This Jupyter notebook analyzes a simulated dataset of running activities to explore VO2 Max trends, including seasonal patterns and heart rate zone correlations. It focuses on key fitness metrics like distance, heart rates, calories, speed, cadence, watts, and VO2 Max. The analysis uses descriptive statistics, visualizations, and basic EDA to derive insights for athletes or coaches.

## Overview
- **Dataset**: "simu_vo2_activities.csv" (~345 rows of simulated running data).
- **Key Sections**:
  1. **Load & Clean Dataset**: Loads CSV, converts "Activity Date" to datetime, selects numeric columns (Distance, Max/Avg Heart Rate, Calories, Average Speed/Cadence/Watts, VO2 Max).
  2. **Summary Statistics**: Prints `describe()` for numeric subset.
  3. **Additional EDA**:
     - Seasonal analysis: Groups VO2 Max by month and plots a bar chart.
     - Heart Rate Zone Analysis: Creates zones (1-5) based on Average Heart Rate; plots boxplot of VO2 Max by zone.
     - Full summary stats table for the dataset.
- **Libraries Used**: pandas, numpy, matplotlib, seaborn, scikit-learn (unused in this version but imported).
- **Outputs**:
  - Numeric summary table (e.g., avg VO2 Max ~32.82, std 5.41).
  - Bar plot: Average VO₂ Max by Month (peaks in certain seasons).
  - Boxplot: VO₂ Max by HR Zone (higher zones correlate with higher VO2).
  - Dataset describe() table (41 columns total).

## Requirements
- Python 3.12+ (tested with 3.13.5).
- Install dependencies:


```python

```
