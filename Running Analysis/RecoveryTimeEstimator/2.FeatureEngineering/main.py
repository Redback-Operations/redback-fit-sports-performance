import os
import functions

# Load the data from the disk
exercise_data, sleep_data = functions.load_data()

# Process the data by selecting only the required variables and get it
user_exercise_logs_new = functions.process_exercise(exercise_data)
user_sleep_logs_new = functions.process_sleep(sleep_data)


# Get the df with the data aggregated by date
exercise_df = functions.aggregate_exercise_logs_by_date(user_exercise_logs_new)
sleep_df = functions.aggregate_sleep_logs_by_date(user_sleep_logs_new)

# combine exercise and sleep dfs by person ID and date
combined_df = functions.merge_exercise_and_sleep(exercise_df, sleep_df)

# save to curated data in the data directory
output_path = "../data/curated"
os.mkdir(output_path)
combined_df.to_csv(f"{output_path}/exercise_sleep_combined.csv", index=False)


















