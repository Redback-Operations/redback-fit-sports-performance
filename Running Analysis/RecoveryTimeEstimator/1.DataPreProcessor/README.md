# Data Pre-Processor

This script processes raw Fitbit data for multiple usersgit commit -m  and generates cleaned JSON files for further analysis.

## Overview

- Iterates through each user directory located under the `../data/raw/` folder.
- Reads `exercise.json` and `sleep.json` files from each user's `fitbit` subfolder.
- Filters and retains only the relevant fields from each file.
- Aggregates the cleaned exercise and sleep data into two separate JSON files located in the `../data/processed/` folder.
- Logs file read and write status messages into the `logs/` directory for tracking and debugging.

## Functionality

- The main script identifies all user directories in `../data/raw/`.
- For each user, it reads the raw exercise and sleep data.
- The `ProcessData` class filters each dataset, extracting only the necessary variables.
- Processed outputs are saved as `exercise.json` and `sleep.json` in the `../data/processed/` directory.
- Log files are created for both exercise and sleep processing to monitor progress and errors.

Download raw data from: [Data](https://datasets.simula.no/pmdata/)

Ensure that raw data is available in the following structure: 
```
data/
└── raw/
    └── user_1/
        └── fitbit/
            ├── exercise.json
            └── sleep.json
    └── user_2/
        └── fitbit/
            ├── exercise.json
            └── sleep.json
```

---

