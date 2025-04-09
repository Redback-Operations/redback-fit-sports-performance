import os
from ProcessData import ProcessData


if __name__ == "__main__":
    # Path to the parent directory containing the folders (data)
    base_path = "data"
    base_path = os.path.join(base_path, "raw")

    # Get the list of directories (people) inside the base directory
    people = [entry.name for entry in os.scandir(base_path) if entry.is_dir()]

    # Pass the list of people to the class which only selects the required variables and combines these variables of all the people
    processed_data = ProcessData(people, base_path)

    # Write the processed data of all the people as individual json files in processed folder
    ProcessData.write_json("exercise.json", processed_data.exercise_processed)
    ProcessData.write_json("sleep.json", processed_data.sleep_processed)

    print("Run Successful!")







