# ReflexionPro Modeling Suite

This folder contains five Jupyter Notebooks and a dataset used for user segmentation, prediction, and scoring in the ReflexionPro ecosystem. The goal of these models is to support a fitness-oriented social platform by helping users understand their activity patterns, get matched with similar users, and stay motivated through insights and comparisons.

---

## 📁 Included Files

- `ImprovedData.xlsx`  
  An anonymized dataset containing exercise information such as steps, calories burned, minutes active, and distance. All models in this suite use this dataset.

- 'activity_metrics.csv'
  An anonymized updated dataset from ImprovedData.xlsx containing exercise information such as steps, calories burned, minutes active, distance with an addition of Overall Activity Score metric column based on the 5.Overall Activity Score Creation ipynb notebook.Estimating Vo2 Max for Dashboard uses this dataset.

- 'activity_metrics_with_vo2.csv'
  An anonymized updated and expanded dataset containing exercise information such as steps, calories burned, minutes active, distance and new feature of Vo2 max added using activity_metrics.csv. Powerbi Dashboard uses this dataset being the most updated and expanded dataset.

---

## 📘 Notebooks Overview

### 1. K-Means Clustering
**Description:**  
This notebook focuses on using K-Means clustering to group exercisers based on their physical engagement. The goal is to categorize users into clusters, where each cluster represents a group of users with similar daily exercise patterns. This clustering helps ReflexionPro users connect with similar individuals for motivation, sending friend requests, and sharing examples to increase engagement and inspiration.

Additionally, this code anonymizes data, creating fictionalized profiles for users while ensuring the architecture can seamlessly incorporate real Garmin/Strava data in the future, once a sufficient amount is collected.

> If you want to experiment with the dataset, skip the early part of the code and go straight to **Start Here**

**Author:** Darren McCauley  
**Date:** April 2025

---

### 2. Calories Regression Model
**Description:**  
This notebook focuses on developing multiple types of regression models to predict calories burned based on user input and available data points. The model will use both known data and theoretical future data points when more live data is uploaded. The purpose is to build a predictive model for caloric expenditure that can be used in ReflexionPro once more live user data becomes available.

Multiple regression techniques will be employed, and the model will evolve with the integration of live data in the future.

**Author:** Darren McCauley  
**Date:** April 2025

---

### 3. DBSCAN Clustering Attempt
**Description:**  
This notebook explores the use of DBSCAN for clustering movement patterns based on the anonymized exercise dataset. While DBSCAN was tested, the results were not especially useful for the final application. This notebook remains here for transparency and documentation of the modeling process.

**Author:** Darren McCauley  
**Date:** April 2025

---

### 4. Input Predictions Model
**Description:**  
This notebook focuses on developing models and equations that enable predicting missing values in daily exercise data. Given three out of the four variables (Steps, Minutes, Calories Burned, Total Distance), the goal is to reasonably predict the missing value based on the available inputs. These models are essential for scenarios where partial data is available, and an educated guess is needed for the missing piece.

**Author:** Darren McCauley  
**Date:** April 2025

---

### 5. Overall Activity Score Creation
**Description:**  
This notebook focuses on creating an Overall Activity Score based on a combination of four key inputs: Steps, Minutes, Calories Burned, and Total Distance. The purpose of this exercise is to establish a standardized score that reflects a user's overall activity level, and to allow users to input their data and receive a percentile comparison to other users' scores. This helps users understand where they stand relative to others in terms of daily activity.

**Author:** Darren McCauley  
**Date:** April 2025

---

### 6. Wearable Performance Insights Dashboard
**Description:**
This is a PowerBi Dashboard created using the activity metrics csv file data with dashboard pages including interactive individual performance insights, interactive performance leaderboard, Average performance metrics on an interactive Map, Scatterplots for comparing various performance metrics against each other using scatterplots where scatter points are the individuals, last dashboard page with distribution of distance active and minutes active among sedentary, light, moderate and very active using pie chart for each individual athlete. This was created for the purpose of integration with the reflexion pro website and includes navigation buttons for the same purpose as well.

**Author:** Madhav Grover  
**Date:** September 2025

---

### 7. Estimating Vo2 Max for Dashboard
**Description:**
This notebook uses activity_metrics.csv to estimate VO2 Max for each individual using metrics in activity_metrics.csv. It calculates a weighted activity score based on very active, fairly active, and lightly active minutes, then normalizes it. A raw VO2 estimate is computed using total distance and scaled to a realistic VO2 Max range. The estimate is further refined based on step counts for improved accuracy. The final dataset, including the refined VO2 Max values, is saved to the activity_metrics_with_vo2.csv.Note:the Vo2 max feature engineered and calculated using this file is an estimate and isn't a measured metric and thus may not be fully accurate.

**Author:** Madhav Grover  
**Date:** September 2025




