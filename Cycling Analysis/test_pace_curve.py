import pandas as pd
import numpy as np
import unittest
from pace_curve import PaceCurveAnalyzer

class TestPaceCurveAnalyzer(unittest.TestCase):

    def setUp(self):
        self.sample_data = pd.DataFrame({
            'Activity Type': ['Run', 'Run', 'Run', 'Run', 'Run', 'Ride', 'Ride', 'Ride', 'Ride', 'Ride'],
            'Activity Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
            'Maximum Pace 5s': [2.50, 2.51, 2.52, 2.56, 2.54, 350, 351, 352, 356, 354],
            'Maximum Pace 10s': [2.40, 2.41, 2.42, 2.46, 2.44, 340, 341, 342, 346, 344],
            'Maximum Pace 30s': [2.30, 2.31, 2.32, 2.36, 2.34, 230, 231, 232, 236, 234],
            'Maximum Pace 1.0min': [2.20, 2.21, 2.22, 2.26, 2.24, 220, 221, 222, 226, 224],
            'Maximum Pace 5.0min': [2.10, 2.11, 2.12, 2.16, 2.14, 210, 211, 212, 216, 214],
            'Maximum Pace 10.0min': [2.05, 2.06, 2.07, 2.11, 2.09, 205, 206, 207, 211, 209],
            'Maximum Pace 20.0min': [2.00, 2.01, 2.02, 2.06, 2.04, 200, 201, 202, 206, 204],
            'Maximum Pace 30.0min': [1.90, 1.91, 1.92, 1.96, 1.94, 190, 191, 192, 196, 194],
            'Maximum Pace 1.0 hr': [1.85, 1.86, 1.87, 1.91, 1.89, 185, 186, 187, 191, 189],
            'Maximum Pace 1.5 hr': [1.80, 1.81, 1.82, 1.86, 1.84, 180, 181, 182, 186, 184],
            'Maximum Pace 2.0 hr': [1.75, 1.76, 1.77, 1.81, 1.79, 175, 176, 177, 181, 179]
        })
        self.analyzer = PaceCurveAnalyzer(data_source=self.sample_data)
        self.error_list =  [(5, np.nan), 
                            (10, np.nan),
                            (30, np.nan),
                            (60, np.nan),
                            (300, np.nan),
                            (600, np.nan),
                            (1200, np.nan),
                            (1800, np.nan),
                            (3600, np.nan),
                            (5400, np.nan),
                            (7200, np.nan)]

    def test_one_day_at_start(self):
        # Test for one day
        activity_type = 'Run'
        date = '2022-01-01'
        num_days = 1
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, [(5, 2.50), 
                                      (10, 2.40), 
                                      (30, 2.30), 
                                      (60, 2.20), 
                                      (300, 2.10), 
                                      (600, 2.05), 
                                      (1200, 2.00), 
                                      (1800, 1.90), 
                                      (3600, 1.85), 
                                      (5400, 1.80), 
                                      (7200, 1.75)])

    def test_one_day_at_start_riding(self):
        # Test for one day
        activity_type = 'Ride'
        date = '2022-01-01'
        num_days = 1
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, [(5, 350), 
                                      (10, 340), 
                                      (30, 230), 
                                      (60, 220), 
                                      (300, 210), 
                                      (600, 205), 
                                      (1200, 200), 
                                      (1800, 190), 
                                      (3600, 185), 
                                      (5400, 180), 
                                      (7200, 175)])

    def test_one_day_in_middle(self):
        # Test for one day
        activity_type = 'Run'
        date = '2022-01-03'
        num_days = 1
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, [(5, 2.52), 
                                      (10, 2.42), 
                                      (30, 2.32), 
                                      (60, 2.22), 
                                      (300, 2.12), 
                                      (600, 2.07), 
                                      (1200, 2.02), 
                                      (1800, 1.92), 
                                      (3600, 1.87), 
                                      (5400, 1.82), 
                                      (7200, 1.77)])

    def test_three_days_at_start(self):
        # Test for one day
        activity_type = 'Run'
        date = '2022-01-01'
        num_days = 3
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, [(5, 2.50), 
                                      (10, 2.40), 
                                      (30, 2.30), 
                                      (60, 2.20), 
                                      (300, 2.10), 
                                      (600, 2.05), 
                                      (1200, 2.00), 
                                      (1800, 1.90), 
                                      (3600, 1.85), 
                                      (5400, 1.80), 
                                      (7200, 1.75)])

    def test_three_days_at_start_riding(self):
        # Test for one day
        activity_type = 'Ride'
        date = '2022-01-01'
        num_days = 3
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, [(5, 350), 
                                      (10, 340), 
                                      (30, 230), 
                                      (60, 220), 
                                      (300, 210), 
                                      (600, 205), 
                                      (1200, 200), 
                                      (1800, 190), 
                                      (3600, 185), 
                                      (5400, 180), 
                                      (7200, 175)])

    def test_three_days_in_middle(self):
        # Test for one day
        activity_type = 'Run'
        date = '2022-01-03'
        num_days = 3
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, [(5, 2.52), 
                                      (10, 2.42), 
                                      (30, 2.32), 
                                      (60, 2.22), 
                                      (300, 2.12), 
                                      (600, 2.07), 
                                      (1200, 2.02), 
                                      (1800, 1.92), 
                                      (3600, 1.87), 
                                      (5400, 1.82), 
                                      (7200, 1.77)])

    def test_three_days_at_end(self):
        # Test for one day
        activity_type = 'Run'
        date = '2022-01-05'
        num_days = 3
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, [(5, 2.56), 
                                      (10, 2.46), 
                                      (30, 2.36), 
                                      (60, 2.26), 
                                      (300, 2.16), 
                                      (600, 2.11), 
                                      (1200, 2.06), 
                                      (1800, 1.96), 
                                      (3600, 1.91), 
                                      (5400, 1.86), 
                                      (7200, 1.81)])

    def test_valid_params(self):
        # Test for valid activity type, date, and num_days
        activity_type = 'Swim'
        date = '2022-01-01'
        num_days = 7
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertIsInstance(pace_curve, list)
        self.assertGreater(len(pace_curve), 0)

    def test_invalid_activity_type(self):
        # Test for invalid activity type
        activity_type = 'Yoga'
        date = '2022-01-01'
        num_days = 7
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, self.error_list)

    def test_invalid_date_format(self):
        # Test for invalid date format
        activity_type = 'Ride'
        date = '22/01/01'
        num_days = 7
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, self.error_list)

    def test_invalid_numdays(self):
        # Test for invalid number of days
        activity_type = 'Ride'
        date = '2022-01-01'
        num_days = -1
        pace_curve = self.analyzer.create_pace_curve(activity_type, date, num_days)
        self.assertEqual(pace_curve, self.error_list)

if __name__ == '__main__':
    unittest.main()