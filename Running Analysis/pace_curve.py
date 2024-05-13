import pandas as pd
import matplotlib.pyplot as plt

class PaceCurveAnalyzer:
    """
    A class for analysing pace curves in running performance data.

    Attributes:
        data_source (pandas.DataFrame): The data source for the analysis.
        distance_buckets (list): List of distance intervals (up to 42 km).

    Methods:
        __init__: Initialises the PaceCurveAnalyzer class.
        create_pace_curve: Creates a pace curve based on activity type, date, and number of days.
        plot_pace_curve: Plots the pace curve.
    """

    def __init__(self, data_source=None):
        self.data_source = data_source
        if self.data_source is None:
            self.data_source = pd.read_csv('https://raw.githubusercontent.com/Redback-Operations/redback-fit-sports-performance/main/Cycling%20Analysis/data/activities_cleaned_TRI001.csv')

        # Distance buckets (in km) up to 42 km (Marathon)
        self.distance_buckets = [1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 42]

    def calculate_pace(self, speed):
        """Calculate pace from speed in minutes per kilometer."""
        return 60 / speed if speed > 0 else None

    def assign_km_bucket(self, distance_km):
        """Assign a run's distance to the nearest appropriate bucket."""
        for bucket in self.distance_buckets:
            if distance_km < bucket:
                return bucket
        return None

    def create_pace_curve(self, activity_type, date, num_days):
        """
        Creates a pace curve based on the specified activity type, date, and number of days.

        Args:
            activity_type (str): The type of activity to filter.
            date (str): The end date for the date range.
            num_days (int): The number of days to include in the date range.

        Returns:
            list: Pairs of distance buckets and maximum (slowest) pace values.
        """
        end_date = pd.to_datetime(date)
        start_date = end_date - pd.Timedelta(days=num_days)

        # Ensure the 'Activity Date' column is in datetime format
        self.data_source['Activity Date'] = pd.to_datetime(self.data_source['Activity Date'])

        # Filter activities based on activity type and date range
        filtered_activities = self.data_source[(self.data_source['Activity Type'] == activity_type) &
                                            (self.data_source['Activity Date'] >= start_date) &
                                            (self.data_source['Activity Date'] <= end_date)].copy()

        # Calculate pace using the `Distance` column already in kilometers
        filtered_activities.loc[:, 'Pace (min/km)'] = (filtered_activities['Elapsed Time'] / 60) / filtered_activities['Distance']

        # Assign each run to a distance bucket
        filtered_activities.loc[:, 'Distance Bucket'] = filtered_activities['Distance'].apply(self.assign_km_bucket)

        # Drop rows with missing or zero distances, speed, or no bucket
        filtered_activities = filtered_activities.dropna(subset=['Distance', 'Pace (min/km)', 'Distance Bucket'])
        filtered_activities = filtered_activities[(filtered_activities['Distance'] > 0) & (filtered_activities['Pace (min/km)'] > 0)]

        # Group by distance bucket and find the average pace per bucket
        pace_curve = filtered_activities.groupby('Distance Bucket')['Pace (min/km)'].mean().reset_index()

        return pace_curve.values.tolist()

    def add_pace_curve_column(self, activity_type, num_days):
        """
        Adds a column to the data source that computes the pace curve for each activity date.

        Args:
            activity_type (str): The type of activity to filter.
            num_days (int): The number of days to include in the date range.

        Returns:
            pandas.DataFrame: The modified DataFrame containing the original columns plus 'Pace Curve'.
        """
        def compute_pace_curve_for_date(row):
            """Helper function to compute the pace curve based on the date of the given row."""
            date = row['Activity Date']
            return self.create_pace_curve(activity_type, date, num_days)

        # Ensure 'Activity Date' is in datetime format
        self.data_source['Activity Date'] = pd.to_datetime(self.data_source['Activity Date'])

        # Apply the helper function to each row and store results in a new column
        self.data_source['Pace Curve'] = self.data_source.apply(compute_pace_curve_for_date, axis=1)

        return self.data_source
    
    def expand_pace_curve_to_columns(self):
        """
        Expands the 'Pace Curve' nested lists into separate rows and columns.
        """
        # Ensure that 'Pace Curve' exists
        if 'Pace Curve' not in self.data_source.columns:
            raise KeyError("Pace Curve column not found. Please run the add_pace_curve_column function first.")

        # Explode the lists into separate rows
        exploded_df = self.data_source.explode('Pace Curve')

        # Convert each pair in 'Pace Curve' to separate columns 'Distance' and 'Pace'
        exploded_df[['Distance', 'Pace']] = pd.DataFrame(exploded_df['Pace Curve'].tolist(), index=exploded_df.index)

        # Drop the original 'Pace Curve' column now that pairs are separated
        exploded_df = exploded_df.drop(columns=['Pace Curve'])

        # Pivot the data to get separate columns for each distance bucket
        final_df = exploded_df.pivot_table(index=exploded_df.index,
                                        columns='Distance',
                                        values='Pace',
                                        aggfunc='first')

        # Rename columns to reflect the distance units (e.g., 'Pace 15 km')
        final_df.columns = [f'Pace {col} km' for col in final_df.columns]

        # Combine the expanded columns with original data, excluding duplicates
        final_df = pd.concat([self.data_source, final_df], axis=1)

        # Reset index if needed to tidy up the DataFrame
        final_df.reset_index(drop=True, inplace=True)

        return final_df

    def plot_pace_curve(self, pace_curve):
        """
        Plots the pace curve.

        Args:
            pace_curve (list): Pairs of distance buckets and maximum (slowest) pace values.

        Returns:
            None
        """
        distances = [pair[0] for pair in pace_curve]
        paces = [pair[1] for pair in pace_curve]

        # Create smoothed data using a rolling mean
        pace_series = pd.Series(paces)
        smooth_paces = pace_series.rolling(window=2, center=True).mean().fillna(pace_series)

        plt.figure(figsize=(10, 6))
        plt.plot(distances, paces, color='lightgrey', label='Original', marker='.')
        plt.plot(distances, smooth_paces, color='blue', label='Smoothed', marker='.')
        plt.xticks(distances)
        plt.xlabel('Distance (km)')
        plt.ylabel('Pace (min/km)')
        plt.title('Pace Curve')
        plt.legend()
        plt.show()
