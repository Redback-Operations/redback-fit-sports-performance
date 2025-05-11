import os, json
import pandas as pd

# Load the data from the processed container inside data directory
def load_data():
    # Resolve absolute path relative to current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, '..', 'data', 'processed')

    with open(os.path.join(path, 'exercise.json'), 'r') as exercise_file:
        exercise_data = json.load(exercise_file)

    with open(os.path.join(path, 'sleep.json'), 'r') as sleep_file:
        sleep_data = json.load(sleep_file)

    return exercise_data, sleep_data


# Process the exercise data by selecting only the relevant variables and get the date separated
def process_exercise(exercise_data):
    exercise_endpoints = [
        "startTime",
        "steps",
        "calories",
        "averageHeartRate",
        "activeDuration",
        "elevationGain"
    ]

    user_exercise_logs_new = {}

    for person in exercise_data:
        for person_key in person.keys():
            person_data = []
            for exercise_log in person[person_key]:
                new_log_data = {}
                for endpoint in exercise_endpoints:
                    if endpoint == "startTime":
                        new_log_data["startDate"] = exercise_log["startTime"].split(" ")[0]
                    else:
                        new_log_data[endpoint] = exercise_log[endpoint]

                person_data.append(new_log_data)

            user_exercise_logs_new[person_key] = person_data

    return user_exercise_logs_new


# Process the exercise data by selecting only the relevant variables
def process_sleep(sleep_data):
    sleep_endpoints = [
        "dateOfSleep",
        "duration",
        "minutesAsleep",
        "minutesAwake",
        "efficiency",
    ]

    user_sleep_logs_new = {}

    for person in sleep_data:
        for person_key in person.keys():
            person_data = []
            for sleep_log in person[person_key]:
                new_log_data = {}
                for endpoint in sleep_endpoints:
                        new_log_data[endpoint] = sleep_log[endpoint]

                person_data.append(new_log_data)

            user_sleep_logs_new[person_key] = person_data

    return user_sleep_logs_new


# Aggregate exercise data with respect to date for each user
def aggregate_exercise_logs_by_date(user_exercise_logs_new):
    # map aggregates
    agg_map = {
        'activeDuration': 'sum',
        'steps': 'sum',
        'calories': 'sum',
        'elevationGain': 'sum',
        'averageHeartRate': 'mean'
    }

    all_agg = []  # will hold one DataFrame per person

    for person_id, logs in user_exercise_logs_new.items():
        # build and aggregate
        df = pd.DataFrame(logs)
        agg_df = df.groupby('startDate', as_index=False).agg(agg_map).round({'elevationGain': 2, 'averageHeartRate': 2})

        # tag with the person
        agg_df['personId'] = person_id

        all_agg.append(agg_df)

    # concatenate into one big DataFrame
    final_df = pd.concat(all_agg, ignore_index=True)

    # reorder columns
    final_df = final_df[
        ['personId', 'startDate', 'activeDuration', 'steps',
         'calories', 'elevationGain', 'averageHeartRate']
    ]

    return final_df

# Aggregate sleep data with respect to date for each user
def aggregate_sleep_logs_by_date(user_sleep_logs_new):
    agg_map = {
        'duration': 'sum',
        'minutesAsleep': 'sum',
        'minutesAwake': 'sum',
        'efficiency': 'mean'
    }

    all_agg = []  # will hold one DataFrame per person

    for person_id, logs in user_sleep_logs_new.items():
        # build and aggregate
        df = pd.DataFrame(logs)
        agg_df = df.groupby('dateOfSleep', as_index=False).agg(agg_map).round({'efficiency': 2})

        # tag with the person
        agg_df['personId'] = person_id

        all_agg.append(agg_df)

    # concatenate into one big DataFrame
    final_df = pd.concat(all_agg, ignore_index=True)

    final_df = final_df[
        ['personId', 'dateOfSleep', 'duration', 'minutesAsleep',
         'minutesAwake', 'efficiency']
    ]

    return final_df


# Merge the two dataframes with inner join by personId and date by and also renaming the columns
def merge_exercise_and_sleep(exercise_df, sleep_df):
    # Change date columns to actual date types
    exercise_df['startDate'] = pd.to_datetime(exercise_df['startDate'])
    sleep_df['dateOfSleep'] = pd.to_datetime(sleep_df['dateOfSleep'])

    # rename and merge on the same column name
    exercise_renamed = exercise_df.rename(columns={
        'startDate': 'date',
        'activeDuration': 'exercise_activeDuration_in_ms',
        'steps': 'exercise_steps',
        'calories': 'exercise_calories',
        'elevationGain': 'exercise_elevationGain',
        'averageHeartRate': 'exercise_averageHeartRate'
    })
    sleep_renamed = sleep_df.rename(columns={
        'dateOfSleep': 'date',
        'duration': 'sleep_duration_in_ms',
        'minutesAsleep': 'sleep_minutesAsleep',
        'minutesAwake': 'sleep_minutesAwake',
        'efficiency': 'sleep_efficiency'
    })
    combined_df = pd.merge(
        exercise_renamed,
        sleep_renamed,
        on=['personId', 'date'],
        how='inner'
    )

    return combined_df

