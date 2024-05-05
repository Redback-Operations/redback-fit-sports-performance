import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

class PaceCurveAnalyzer:
    """
    A class for analyzing pace curves in swimming, cycling and running performance data.

    Attributes:
        data_source (pandas.DataFrame): The data source for the analysis.
        durations (list): A list of durations for pace calculation.
        pace_fields (list): A list of pace field names.

    Methods:
        __init__: Initializes the PaceCurveAnalyzer class.
        format_duration: Formats the duration in seconds to a human-readable format.
        create_pace_curve: Creates a pace curve based on activity type, date, and number of days.
        plot_pace_curve: Plots the pace curve.

    """

    def __init__(self, data_source=None):
        self.data_source = data_source
        if self.data_source is None:
            self.data_source = pd.read_csv('data/extended_activities_TRI001.csv')

        self.durations = [5, 10, 30, 60, 5*60, 10*60, 20*60, 30*60, 60*60, 90*60, 120*60]
        self.pace_fields = ['Maximum Pace 5s', 
                            'Maximum Pace 10s', 
                            'Maximum Pace 30s', 
                            'Maximum Pace 1.0min', 
                            'Maximum Pace 5.0min', 
                            'Maximum Pace 10.0min', 
                            'Maximum Pace 20.0min', 
                            'Maximum Pace 30.0min', 
                            'Maximum Pace 1.0hr', 
                            'Maximum Pace 1.5hr', 
                            'Maximum Pace 2.0hr'
                            ]


    def format_duration(self, seconds):
        """
        Formats the duration in seconds to a human-readable format.

        Args:
            seconds (int): The duration in seconds.

        Returns:
            str: The formatted duration.
        """

        if seconds < 60:
            return f"{seconds}s"
        elif seconds < 3600:
            return f"{seconds / 60:.1f}min"
        else:
            return f"{seconds / 3600:.1f} hr"


    def create_pace_curve(self, activity_type, date, num_days):
        """
        Creates a pace curve based on the specified activity type, date, and number of days.

        Args:
            activity_type (str): The type of activity to filter.
            date (str): The end date for the date range.
            num_days (int): The number of days to include in the date range.

        Returns:
            list: A list of pairs of duration and maximum pace values.
        """

        # Read the data from the file
        data = self.data_source

        # Convert date to datetime
        end_date = pd.to_datetime(date)
        start_date = end_date - pd.Timedelta(days=num_days)

        # Convert 'Activity Date' column to datetime
        data['Activity Date'] = pd.to_datetime(data['Activity Date'])

        # Filter the activities based on the activity type and date range
        filtered_activities = data[(data['Activity Type'] == activity_type) & 
                                   (data['Activity Date'] >= start_date) & 
                                   (data['Activity Date'] <= end_date)]

        pace_curve = []
        for duration in self.durations:
            # Create a column name based on duration
            col_name = f'Maximum Pace {self.format_duration(duration)}'

            # Check if the column exists in the data
            if col_name in filtered_activities.columns:
                # Find the highest value for the 'Maximum Pace...' field for this duration
                max_pace = filtered_activities[col_name].max()
                pace_curve.append((duration, max_pace))
            else:
                # Handle cases where the column does not exist (e.g., append a default value or skip)
                pace_curve.append((duration, None))  

        return pace_curve


    def plot_pace_curve(self, pace_curve, tested_cp):
        """
        Plots the pace curve.

        Args:
            pace_curve (list): A list of pairs of duration and maximum pace values.
            tested_cp (float): The tested Critical Power.

        Returns:
            None
        """

        filtered_durations = []
        filtered_pacess = []

        for duration, pace in pace_curve:
            if pace > 0:
                filtered_durations.append(self.format_duration(duration))
                filtered_paces.append(pace)

        # Convert durations to a numeric format
        numeric_durations = np.arange(len(filtered_durations))

        # Convert the list to a Pandas Series for easy rolling mean computation
        pace_series = pd.Series(filtered_paces)

        # Compute the moving average (rolling mean)
        # The window size determines the smoothing level
        smooth_paces = pace_series.rolling(window=2, center=True).mean().fillna(pace_series)

        # Plotting the original and smoothed curve
        plt.figure(figsize=(10, 6))
        plt.plot(numeric_durations, filtered_paces, color='lightgrey', label='Original', marker='.')
        plt.plot(numeric_durations, smooth_paces, color='blue', label='Smoothed', marker='.')
        plt.axhline(y=tested_cp, color='g', linestyle='--', label='Tested CP')
        plt.xticks(numeric_durations, filtered_durations)
        plt.xlabel('Duration')
        plt.ylabel('Pace (m/s)')
        plt.title('Pace Curve')
        plt.legend()
        plt.show()

