import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
class PowerCurveAnalyzer:
    """
    A class for analyzing power curves in cycling performance data.

    Attributes:
        data_source (pandas.DataFrame): The data source for the analysis.
        durations (list): A list of durations for power calculation.
        power_fields (list): A list of power field names.

    Methods:
        __init__: Initializes the PowerCurveAnalyzer class.
        format_duration: Formats the duration in seconds to a human-readable format.
        create_power_curve: Creates a power curve based on activity type, date, and number of days.
        plot_power_curve: Plots the power curve.

    """

    def __init__(self, data_source=None):
        self.data_source = data_source
        if self.data_source is None:
            self.data_source = pd.read_csv('data/extended_activities.csv')

        self.durations = [5, 10, 30, 60, 5*60, 10*60, 20*60, 30*60, 60*60, 90*60, 120*60]
        self.power_fields = ['Maximum Power 5s', 
                             'Maximum Power 10s', 
                             'Maximum Power 30s', 
                             'Maximum Power 1.0min', 
                             'Maximum Power 5.0min', 
                             'Maximum Power 10.0min', 
                             'Maximum Power 20.0min', 
                             'Maximum Power 30.0min', 
                             'Maximum Power 1.0hr', 
                             'Maximum Power 1.5hr', 
                             'Maximum Power 2.0hr'
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


    def create_power_curve(self, activity_type, date, num_days):
        """
        Creates a power curve based on the specified activity type, date, and number of days.

        Args:
            activity_type (str): The type of activity to filter.
            date (str): The end date for the date range.
            num_days (int): The number of days to include in the date range.

        Returns:
            list: A list of pairs of duration and maximum power values.
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

        power_curve = []
        for duration in self.durations:
            # Create a column name based on duration
            col_name = f'Maximum Power {self.format_duration(duration)}'

            # Check if the column exists in the data
            if col_name in filtered_activities.columns:
                # Find the highest value for the 'Maximum Power...' field for this duration
                max_power = filtered_activities[col_name].max()
                power_curve.append((duration, max_power))
            else:
                # Handle cases where the column does not exist (e.g., append a default value or skip)
                power_curve.append((duration, None))  # or continue, based on desired behavior

        return power_curve


    def plot_power_curve(self, power_curve, tested_ftp):
        """
        Plots the power curve.

        Args:
            power_curve (list): A list of pairs of duration and maximum power values.
            tested_ftp (float): The tested FTP (Functional Threshold Power).

        Returns:
            None
        """

        filtered_durations = []
        filtered_powers = []

        for duration, power in power_curve:
            if power > 0:
                filtered_durations.append(self.format_duration(duration))
                filtered_powers.append(power)

        # Convert durations to a numeric format
        numeric_durations = np.arange(len(filtered_durations))

        # Convert the list to a Pandas Series for easy rolling mean computation
        power_series = pd.Series(filtered_powers)

        # Compute the moving average (rolling mean)
        # The window size determines the smoothing level
        smooth_powers = power_series.rolling(window=2, center=True).mean().fillna(power_series)

        # Plotting the original and smoothed curve
        plt.figure(figsize=(10, 6))
        plt.plot(numeric_durations, filtered_powers, color='lightgrey', label='Original', marker='.')
        plt.plot(numeric_durations, smooth_powers, color='blue', label='Smoothed', marker='.')
        plt.axhline(y=tested_ftp, color='g', linestyle='--', label='Tested FTP')
        plt.xticks(numeric_durations, filtered_durations)
        plt.xlabel('Duration')
        plt.ylabel('Power (Watts)')
        plt.title('Power Curve')
        plt.legend()
        plt.show()

