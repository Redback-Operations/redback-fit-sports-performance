import os, json

# Class to process the data based on the list and path of the data folder
class ProcessData:
    def __init__(self, people, base_path):
        self.people = people
        self.base_path = base_path

        # Required exercise and sleep variables
        self.exercise_endpoints = [
            "logId",
            "activityName",
            "startTime",
            "activityTypeId",
            "duration",
            "steps",
            "calories",
            "averageHeartRate",
            "heartRateZones",
            "activeDuration",
            "elevationGain",
            "activityLevel"
        ]

        self.sleep_endpoints = [
            "logId",
            "dateOfSleep",
            "startTime",
            "endTime",
            "duration",
            "minutesAsleep",
            "minutesAwake",
            "timeInBed",
            "efficiency",
            "type",
            "levels_summary",
            "mainSleep"
        ]
        
        # Get the processed json
        self.exercise_processed = []
        self.sleep_processed = []

        for person in self.people:
            self.person = person

            self.exercise_raw, self.sleep_raw = self.get_data(self.base_path)

            self.exercise_processed_dict = {}
            self.sleep_processed_dict = {}

            self.exercise_processed_dict[self.person] = self.filter_exercise(self.exercise_raw)
            self.sleep_processed_dict[person] = self.filter_sleep(self.sleep_raw)

            self.exercise_processed.append(self.exercise_processed_dict)
            self.sleep_processed.append(self.sleep_processed_dict)


    def get_data(self, base_directory):
        # Interested files
        endpoints = ["exercise.json", "sleep.json"]
        endpoints_values = []

        # Directory structure
        folder_path_local = os.path.join(base_directory, self.person, 'fitbit')

        for endpoint in endpoints:
            file_path_local = os.path.join(folder_path_local, endpoint)

            # Check if the file exists in the folder
            if os.path.exists(file_path_local):
                with open(file_path_local, 'r') as file:
                    data = json.load(file)
                    endpoints_values.append(data)
                    log = f"{file_path_local} - Read okay"
                    ProcessData.write_log(endpoint, log)
            else:
                log = f"File {endpoint} not found for {self.person}"
                ProcessData.write_log(endpoint, log)

        # Ensure we always return two values, even if one file is missing
        while len(endpoints_values) < 2:
            endpoints_values.append(None)

        return endpoints_values[0], endpoints_values[1]
   
   # Filter exercise based on input
    def filter_exercise(self, exercise_data):
        filtered_exercise = []

        for exercise in exercise_data:
            individual_exercise = {}

            for endpoint in self.exercise_endpoints:
                individual_exercise[endpoint] = exercise.get(endpoint)

            filtered_exercise.append(individual_exercise)

        return filtered_exercise

    # Filter sleep based on input
    def filter_sleep(self, sleep_data):
        filtered_sleep = []

        for sleep in sleep_data:
            individual_sleep = {}

            for endpoint in self.sleep_endpoints:
                if endpoint == "levels_summary":
                    individual_sleep[endpoint] = sleep.get("levels", {}).get("summary")
                else:
                    individual_sleep[endpoint] = sleep.get(endpoint)

            filtered_sleep.append(individual_sleep)

        return filtered_sleep
    
    # Write functions
    @staticmethod
    def write_json(filename, content):
        path = f"../data/processed/{filename}"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w') as file:
            json.dump(content, file)
            log = f"{filename} - write okay"
            ProcessData.write_log(filename, log)

    @staticmethod
    def write_log(name, content):
        log_file = f"{name.split('.')[0]}_log.txt"
        path = f"logs/{log_file}"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'a') as file:
            file.write(content + "\n")


