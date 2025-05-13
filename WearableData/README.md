# ReflexionPro Modeling Suite

This folder contains five Jupyter Notebooks and a dataset used for user segmentation, prediction, and scoring in the ReflexionPro ecosystem. The goal of these models is to support a fitness-oriented social platform by helping users understand their activity patterns, get matched with similar users, and stay motivated through insights and comparisons.

---

## 📁 Included Files

- `ImprovedData.xlsx`  
  An anonymized dataset containing exercise information such as steps, calories burned, minutes active, and distance. All models in this suite use this dataset.

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
