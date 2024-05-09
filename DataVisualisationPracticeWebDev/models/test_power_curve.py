import pandas as pd
import numpy as np
import unittest
from power_curve import PowerCurveAnalyzer

class TestPowerCurveAnalyzer(unittest.TestCase):

    def setUp(self):
        self.sample_data = pd.DataFrame({
            'Activity Type': ['Ride', 'Ride', 'Ride', 'Ride', 'Ride'],
            'Activity Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
            'Maximum Power 5s': [250, 251, 252, 256, 254],
            'Maximum Power 10s': [240, 241, 242, 246, 244],
            'Maximum Power 30s': [230, 231, 232, 236, 234],
            'Maximum Power 1.0min': [220, 221, 222, 226, 224],
            'Maximum Power 5.0min': [210, 211, 212, 216, 214],
            'Maximum Power 10.0min': [205, 206, 207, 211, 209],
            'Maximum Power 20.0min': [200, 201, 202, 206, 204],
            'Maximum Power 30.0min': [190, 191, 192, 196, 194],
            'Maximum Power 1.0 hr': [185, 186, 187, 191, 189],
            'Maximum Power 1.5 hr': [180, 181, 182, 186, 184],
            'Maximum Power 2.0 hr': [175, 176, 177, 181, 179]
        })
        self.analyzer = PowerCurveAnalyzer(data_source=self.sample_data)
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
        activity_type = 'Ride'
        date = '2022-01-01'
        num_days = 1
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertEqual(power_curve, [(5, 250), (10, 240), (30, 230), (60, 220), (300, 210), (600, 205), (1200, 200), (1800, 190), (3600, 185), (5400, 180), (7200, 175)])

    def test_one_day_in_middle(self):
        # Test for one day
        activity_type = 'Ride'
        date = '2022-01-03'
        num_days = 1
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertEqual(power_curve, [(5, 252), (10, 242), (30, 232), (60, 222), (300, 212), (600, 207), (1200, 202), (1800, 192), (3600, 187), (5400, 182), (7200, 177)])

    def test_three_days_at_start(self):
        # Test for one day
        activity_type = 'Ride'
        date = '2022-01-01'
        num_days = 3
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertEqual(power_curve, [(5, 250), (10, 240), (30, 230), (60, 220), (300, 210), (600, 205), (1200, 200), (1800, 190), (3600, 185), (5400, 180), (7200, 175)])

    def test_three_days_in_middle(self):
        # Test for one day
        activity_type = 'Ride'
        date = '2022-01-03'
        num_days = 3
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertEqual(power_curve, [(5, 252), (10, 242), (30, 232), (60, 222), (300, 212), (600, 207), (1200, 202), (1800, 192), (3600, 187), (5400, 182), (7200, 177)])

    def test_three_days_at_end(self):
        # Test for one day
        activity_type = 'Ride'
        date = '2022-01-05'
        num_days = 3
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertEqual(power_curve, [(5, 256), (10, 246), (30, 236), (60, 226), (300, 216), (600, 211), (1200, 206), (1800, 196), (3600, 191), (5400, 186), (7200, 181)])

    def test_valid_params(self):
        # Test for valid activity type, date, and num_days
        activity_type = 'Ride'
        date = '2022-01-01'
        num_days = 7
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertIsInstance(power_curve, list)
        self.assertGreater(len(power_curve), 0)

    def test_invalid_activity_type(self):
        # Test for invalid activity type
        activity_type = 'Running'
        date = '2022-01-01'
        num_days = 7
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertEqual(power_curve, self.error_list)

    def test_invalid_date_format(self):
        # Test for invalid date format
        activity_type = 'Ride'
        date = '22/01/01'
        num_days = 7
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertEqual(power_curve, self.error_list)

    def test_invalid_numdays(self):
        # Test for invalid number of days
        activity_type = 'Ride'
        date = '2022-01-01'
        num_days = -1
        power_curve = self.analyzer.create_power_curve(activity_type, date, num_days)
        self.assertEqual(power_curve, self.error_list)

if __name__ == '__main__':
    unittest.main()