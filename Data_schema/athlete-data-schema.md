# Running_Athlete Performance Management Data Schema_Project 3

This document explains the structure of our athlete performance management data schema, categorised into four main types of data, and provides the full JSON schema for implementation.

## Data Categories

1. User and Descriptive Data
2. Data Generated from the Actual Activity
3. Data Generated Post-Activity (Summaries)
4. Data Generated from Activity (Body Insight)

## 1. User and Descriptive Data


This category includes information that is attached to activities and summaries, providing context about the user and the activity.

### Metadata
- `datetime`: Timestamp of the activity
- `userId`: Unique identifier for the athlete
- `acitivityID`: Unique identifier for the activity
- `activityName`: Activity name
- `activityType`: Activity type
- `description`: Short description of the activity
### Athlete Profile
- `name`: Athlete's name
- `age`: Athlete's age
- `gender`: Athlete's gender
- `height`: Athlete's height
- `weight`: Athlete's weight

### Geographiccal Data
- `temperature`: Ambient temperature during the activity
- `humidity`: Humidity level during the activity
- `windSpeed`: Wind speed during the activity
- `windDirection`: Win direction during the activity
- `begin_longtitude`: Begin longtitude of the activity location
- `end_longtitude`: End longtitude of the activity location
- `begin_lattitude`: Begin lattitude of the activity location
- `end_lattitude`: End lattitude of the activity location
- `condition`: Weather condition on the activity day (e.g "fair")
- `rainfall`: Rainfall Condition (e.g "no")

## 2. Data Generated from the Activity

This category includes real-time data collected during the running activity.

### Activity Data (summary)
- `beginTime`: Specific time point at the start of  the activity (e.g "Fri Aug 9, 2024, 12:00")
- `endTime`:  Specific time point at the end of the activity
- `activityType`: Type of activity performed (e.g "Running")
- `averageSpeed`: Average speed during the activity 
- `maxSpeed`: Maximum speed during the activity
- `averageHeartRate`: Average heart rate during the activity
- `maxHeartRate`: Maximum heart rate during the activity
- `calories`: Calories burnt during the activity
- `duration`: Duration of the activity (e.g "0:59:03")
- `movingDuration`: Duration of the activity while the athlete was moving 
- `averageMovingSpeed`: Average moving speed of the activty
- `distance`: Total distance covered in the activity
- `elevationGain`: Maximum elevation reached during the activity
- `elevationLoss`: Total elevation loss during the activity
- `maxElevation`: Total elevation gain during the activity
- `minElevation`: Minumum elevation reached during the activity

### Activity Data (Time Series)
- `timestamp`: Specific time point during the activity
- `longtitude`: Longtitude at a specific time point
- `lattitude`: Lattitude at a specific time point
- `elevation`: Elevation at a specific time point
- `heartRate`: Heart rate at a specific time point
- `cadence`: Cadence at a specific time point

## 3. Data Generated Post-Run (Summaries)

This category includes data that is calculated or estimated after the run is completed.

### Physiological Measurements
- `trainingStatus`: Overall training condition (e.g "intensed")
- `bodyBattery`: Measure of energy level (e.g "75")
- `recoveryTime`: Estimated time needed for full recovery 
- `trainingLoad`: Quantification of training stress
- `trainingLoadFocus`: Primary training benefit (e.g., endurance, speed)
- `trainingEffect`: 
  - `aerobic`: Impact on aerobic fitness
  - `anaerobic`: Impact on anaerobic fitness
- `hrv`: Heart rate variability 
- `hrZones`: Heart rate zones 
- `hydrationStatus`: Hydration status
- `Epoc`: Excess post-exercise oxygen consumption

## 4. Data Generated from Activity (Body Insight)

This category includes performance metrics and estimations derived from the activity data.

### Performance Metrics
- `vo2Max`: Estimated maximum oxygen uptake
- `lactateThreshold`: Estimated pace at lactate threshold
- `raceTimePrediction`: Predicted times for various race distances
- `realTimeStamina`: Estimated remaining endurance
- `functionalThresholdPower`: Power output at lactate threshold
- `powerToWeightRatio`: Power output relative to body weight
- `criticalPower`: Highest power that can be maintained for a given duration
- `peakPower`: Highest power output for various durations (5s, 1min, 5min, 20min)
- `thresholdHeartRate`: Heart rate at lactate threshold
- `performanceIndex`: Overall performance score
- `fatigueIndex`: Measure of accumulated fatigue

### Acclimation and Readiness
- `heatAcclimation`: Level of adaptation to hot conditions
- `altitudeAcclimation`: Level of adaptation to high altitude
- `trainingReadiness`: Overall readiness for training
- `enduranceScore`: Measure of endurance capability

## Full JSON Schema

Below is the complete JSON schema for the Athlete Performance Management Data:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "metadata": {
      "type": "object",
      "properties": {
        "activityId": { "type": "string" },
        "activityName": { "type": "string" },
        "description": { "type": "string" },
        "beginTime": { "type": "string", "format": "date-time" },
        "endTime": { "type": "string", "format": "date-time" },
        "userId": { "type": "string" },
        "activityType": { "type": "string" },
      },
      "required": [
        "activityId",
        "activityName",
        "description",
        "beginTime",
        "endTime",
        "userId",
        "activityType",
      ]
    },
    "athleteProfile": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "age": { "type": "integer" },
        "gender": { "type": "string" },
        "height": { "type": "number" },
        "weight": { "type": "number" }
      }
    },
    "geographicalData": {
      "type": "object",
      "properties": {
        "temperature": { "type": "number" },
        "humidity": { "type": "number" },
        "windSpeed": { "type": "number" },
        "windDirection": { "type": "string" },
        "beginLongitude": { "type": "number" },
        "endLongitude": { "type": "number" },
        "beginLatitude": { "type": "number" },
        "endLatitude": { "type": "number" },
        "condition": { "type": "string" },
        "rainfall": { "type": "string" },
      },
      "required": [
        "temperature",
        "humidity",
        "windSpeed",
        "windDirection",
        "beginLongitude",
        "endLongitude",
        "beginLatitude",
        "endLatitude",
        "condition",
        "rainfall"
      ]
    },
    "activityDataSummary": {
      "type": "object",
      "properties": {
        "averageSpeed": { "type": "number" },
        "maxSpeed": { "type": "number" },
        "averageHeartRate": { "type": "number" },
        "maxHeartRate": { "type": "number" },
        "calories": { "type": "number" },
        "duration": { "type": "string" },
        "durationSeconds": { "type": "number" },
        "movingDuration": { "type": "string" },
        "movingDurationSeconds": { "type": "number" },
        "averageMovingSpeed": { "type": "number" },
        "distance": { "type": "number" },
        "maxElevation": { "type": "number" },
        "minElevation": { "type": "number" },
        "elevationGain": { "type": "number" },
        "elevationLoss": { "type": "number" }
        
      },
      "required": [
        "averageSpeed",
        "maxSpeed",
        "averageHeartRate",
        "maxHeartRate",
        "calories",
        "duration",
        "movingDuration",
        "averageMovingSpeed",
        "distance"
        "maxElevation",
        "minElevation",
        "elevationGain",
        "elevaionLoss"
      ]
    },
    "activityDataTimeSeries": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "timestamp": { "type": "string", "format": "date-time" },
          "longitude": { "type": "number" },
          "latitude": { "type": "number" },
          "elevation": { "type": "number" },
          "heartRate": { "type": "number" },
          "cadence": { "type": "number" }
        },
        "required": [
          "timestamp",
          "longitude",
          "latitude",
          "elevation",
          "heartRate",
          "cadence"
        ]
      }
    },
    "physiologicalMeasurements": {
      "type": "object",
      "properties": {
        "trainingStatus": { "type": "string" },
        "bodyBattery": { "type": "number" },
        "recoveryTime": { "type": "number" },
        "trainingLoad": { "type": "number" },
        "trainingLoadFocus": { "type": "string" },
        "trainingEffect": {
          "type": "object",
          "properties": {
            "aerobic": { "type": "number" },
            "anaerobic": { "type": "number" }
          }
        },
        "hrv": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "timestamp": { "type": "string", "format": "date-time" },
              "value": { "type": "number" }
            }
          }
        },
        "hrZones": { "type": "object" },
        "calories": { "type": "number" },
        "hydrationStatus": { "type": "number" },
        "epoc": { "type": "number" }
      },
      "required": [
        "trainingStatus",
        "bodyBattery",
        "recoveryTime",
        "trainingLoad",
        "trainingLoadFocus",
        "trainingEffect",
        "hrv",
        "calories",
        "hydrationStatus",
        "epoc"
      ]
    },
    "performanceMetrics": {
      "type": "object",
      "properties": {
        "vo2Max": { "type": "number" },
        "lactateThreshold": { "type": "number" },
        "raceTimePrediction": { "type": "string" },
        "realTimeStamina": { "type": "number" },
        "functionalThresholdPower": { "type": "number" },
        "powerToWeightRatio": { "type": "number" },
        "criticalPower": { "type": "number" },
        "peakPower": {
          "type": "object",
          "properties": {
            "fiveSeconds": { "type": "number" },
            "oneMinute": { "type": "number" },
            "fiveMinutes": { "type": "number" },
            "twentyMinutes": { "type": "number" }
          }
        },
        "thresholdHeartRate": { "type": "number" },
        "performanceIndex": { "type": "number" },
        "fatigueIndex": { "type": "number" }
      },
      "required": [
        "vo2Max",
        "lactateThreshold",
        "raceTimePrediction",
        "realTimeStamina",
        "functionalThresholdPower",
        "powerToWeightRatio",
        "criticalPower",
        "peakPower",
        "thresholdHeartRate",
        "performanceIndex",
        "fatigueIndex"
      ]
    },
    "acclimationAndReadiness": {
      "type": "object",
      "properties": {
        "heatAcclimation": { "type": "number" },
        "altitudeAcclimation": { "type": "number" },
        "trainingReadiness": { "type": "number" },
        "enduranceScore": { "type": "number" }
      },
      "required": [
        "heatAcclimation",
        "altitudeAcclimation",
        "trainingReadiness",
        "enduranceScore"
      ]
    }
  },
  "required": [
    "metadata",
    "athleteProfile",
    "geographicalData",
    "activityDataSummary",
    "activityDataTimeSeries",
    "physiologicalMeasurements",
    "performanceMetrics",
    "acclimationAndReadiness"
  ]
}
```