import requests

def call_swim_duration_api(distance, paces):
    # URL of the API Endpoint
    url = "https://127.0.0.1:5000/swim-duration/predict"
    
    # Data payload in JSON format
    payload = {
        "distance": distance,
        "paces": paces
    }
    
    # Sending a POST request to the Flask API
    response = requests.post(url, json=payload)
    
    # Checking the response from the server
    if response.status_code == 200:
        print("API call successful.")
        print("Response:", response.json())
    else:
        print("API call failed.")
        print("Status Code:", response.status_code)
        print("Error:", response.json())

# Example distance and paces
distance_example = 1500
pace_curve_example = [
    {"pace": "Maximum Pace 5s", "speed": 4.5},
    {"pace": "Maximum Pace 10s", "speed": 4.7},
    {"pace": "Maximum Pace 30s", "speed": 4.8},
    {"pace": "Maximum Pace 1.0min", "speed": 5.0},
    {"pace": "Maximum Pace 5.0min", "speed": 5.2},
    {"pace": "Maximum Pace 10.0min", "speed": 5.4},
    {"pace": "Maximum Pace 20.0min", "speed": 5.6},
    {"pace": "Maximum Pace 30.0min", "speed": 5.8},
    {"pace": "Maximum Pace 1.0 hr", "speed": 6.0},
    {"pace": "Maximum Pace 1.5 hr", "speed": 6.2},
    {"pace": "Maximum Pace 2.0 hr", "speed": 6.4}
]

# Call the Swim Duration prediction API
print("Calling Swim Duration prediction endpoint.")
call_swim_duration_api(distance_example, pace_curve_example)
print("Script finished.")
