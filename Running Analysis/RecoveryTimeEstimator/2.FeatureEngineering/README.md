# Feature Engineering

## Introduction  
This code transforms preprocessed Fitbit exercise and sleep logs into a unified, analysis‑ready dataset. Raw JSON exports—each indexed by user—are stored in the `data/processed` directory. The resulting output consolidates daily activity and rest metrics into a single table, facilitating downstream statistical analysis and machine learning applications.

## Overview  
The integration workflow comprises four principal stages:

1. **Data Ingestion**  
   Reads the `exercise.json` and `sleep.json` files from the `data/processed` folder, loading each into memory as native Python structures.

2. **Record Transformation**  
   Filters each user’s logs to retain only relevant fields.  
   - **Exercise**: date, steps, calories, active duration, elevation gain, average heart rate.  
   - **Sleep**: date of sleep, total duration, minutes asleep/awake, sleep efficiency.  
   All timestamps are normalized to date format for consistency.

3. **Daily Aggregation**  
   Groups records by user and date:  
   - Sums values for durations, steps, calories, sleep minutes, and wake minutes.  
   - Computes mean values for heart rate and sleep efficiency.  
   Elevation gain and efficiency are rounded to two decimal places.

4. **Cross‑Dataset Merge**  
   Aligns aggregated exercise and sleep summaries by `personId` and date:  
   - Converts date fields to `datetime`.  
   - Renames columns with `exercise_` or `sleep_` prefixes for clarity.  
   - Performs an inner join, yielding only those days with both activity and rest data.

## Functionality  

| Function                                 | Description                                                                                          |
|------------------------------------------|------------------------------------------------------------------------------------------------------|
| **load_data()**                          | Loads preprocessed JSON logs from `data/processed`.                                                  |
| **process_exercise(exercise_data)**      | Extracts and formats exercise entries, splitting timestamps into date strings.                       |
| **process_sleep(sleep_data)**            | Extracts and formats sleep entries, preserving date and key rest metrics.                            |
| **aggregate_exercise_logs_by_date()**    | Aggregates exercise metrics by user and date; applies sum or mean operations and rounds results.     |
| **aggregate_sleep_logs_by_date()**       | Aggregates sleep metrics by user and date; applies sum or mean operations and rounds efficiency.     |
| **merge_exercise_and_sleep()**           | Joins the two aggregated tables on `personId` and date, renames columns, and returns the merged set.|

The final artifact, `exercise_sleep_combined.csv`, is written to the `data/curated` directory and presents one record per user per day, encompassing both exercise and sleep dimensions.  
