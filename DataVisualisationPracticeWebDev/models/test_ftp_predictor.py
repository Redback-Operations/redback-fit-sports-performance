import unittest
import pandas as pd
from ftp_predictor import FtpPredictor

# Define the data for the test cases
testdata = pd.DataFrame({
   'Activity Date': ['2020-02-04 03:50:34', '2020-02-07 00:22:14', '2020-02-16 03:43:38', 
                      '2020-02-17 22:31:19', '2020-05-20 04:57:24', '2022-09-10 02:55:40', 
                      '2022-12-23 22:59:16', '2023-03-11 00:00:57', '2023-05-04 04:18:44', 
                      '2023-11-18 00:01:54'],
    'Elapsed Time': [7986, 7998, 5725, 5627, 6888, 14090, 8278, 14351, 7496, 22391],
    'Distance': [47.71, 51.69, 42.75, 40.06, 53.27, 99.99, 59.56, 107.22, 55.62, 150.03],
    'Max Heart Rate': [144.0, 140.0, 144.0, 133.0, 136.0, 142.0, 139.0, 150.0, 137.0, 142.0],
    'Relative Effort': [29.0, 24.0, 29.0, 16.0, 24.0, 42.0, 21.0, 49.0, 24.0, 68.0],
    'Athlete Weight': [80.0, 80.0, 80.0, 80.0, 80.0, None, None, None, None, None],
    'Bike Weight': [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0],
    'Moving Time': [7199.0, 7414.0, 5561.0, 5486.0, 6832.0, 13370.0, 7822.0, 13685.0, 7191.0, 21208.0],
    'Max Speed': [12.1, 11.5, 11.1, 9.9, 10.4, 12.305469, 12.396093, 13.921875, 16.855999, 16.904688],
    'Average Speed': [6.648, 6.999, 7.693, 7.403, 7.8, 7.478978, 7.61445, 7.834877, 7.734912, 7.074378],
    'Elevation Gain': [98.0, 176.0, 6.0, 39.0, 12.0, 219.0, 167.0, 170.0, 6.0, 567.370667],
    'Elevation Loss': [80.0, 173.0, 0.0, 46.0, 7.0, 228.0, 186.0, 188.0, 4.0, 568.470642],
    'Elevation Low': [-14.0, 55.0, 11.0, -1.0, 18.4, 21.799999, 13.8, -8.4, 36.599998, 4.8],
    'Elevation High': [12.0, 83.0, 17.0, 12.0, 27.4, 61.599998, 41.200001, 23.0, 44.799999, 103.900002],
    'Max Grade': [18.200001, 12.3, 6.6, 10.8, 2.9, 12.848168, 8.114106, 12.367147, 5.628457, 11.941490],
    'Average Grade': [0.03563, 0.007738, 0.009355, -0.017471, 0.007508, -0.008, -0.009066, 0.007088, -0.00036, -0.000733],
    'Max Cadence': [94.0, 98.0, 148.0, 132.0, 150.0, 154.0, 141.0, 130.0, 119.0, 142.0],
    'Average Cadence': [73.091797, 75.483864, 72.297432, 74.596642, 72.677689, 63.167191, 71.399788, 71.284042, 64.935791, 62.837536],
    'Average Heart Rate': [121.0, 113.0, 126.0, 110.0, 118.0, 107.018806, 104.121254, 115.897774, 114.339043, 111.200958],
    'Average Watts': [123.109879, 126.360954, 133.125656, 133.842712, 167.564514, 160.677032, 154.714493, 154.654816, 151.415649, 132.950958],
    'Calories': [587.0, 342.0, 762.0, 181.0, 390.0, 2119.0, 1197.0, 2114.0, 1090.0, 3895.0],
    'Average Temperature': [20.0, 25.0, 26.0, 18.0, 12.0, 11.0, 18.0, 18.0, 12.0, 17.0],
    'Total Work': [724249.0, 746630.0, 758704.0, 742595.0, 1139882.0, 2119288.0, 1197393.0, 2113952.0, 1089758.0, None],
    'Perceived Exertion': [None, None, None, None, None, None, None, None, None, None],
    'Weighted Average Power': [130.0, 137.0, 140.0, 140.0, 172.0, 168.0, 161.0, 160.0, 152.0, 138.0],
    'Power Count': [7987.0, 7970.0, 5726.0, 5628.0, 6889.0, 13961.0, 8279.0, 14352.0, 7497.0, 22392.0],
    'Prefer Perceived Exertion': [None, None, None, None, None, None, None, None, None, None],
    'Perceived Relative Effort': [None, None, None, None, None, None, None, None, None, None],
    'Grade Adjusted Distance': [None, None, None, None, None, None, None, None, None, None],
    'Average Elapsed Speed': [None, None, None, None, None, 7.096802, 7.195003, 7.471277, 7.420191, 6.700612],
    '60 Day Maximum Power 5s': [514.4, 514.4, 514.4, 514.4, 524.4, 414.2, 655.4, 536.8, 536.8, 361.6],
    '60 Day Maximum Power 10s': [452.0, 452.0, 452.0, 452.0, 454.3, 352.5, 637.4, 443.8, 417.6, 333.8],
    '60 Day Maximum Power 30s': [342.1, 342.1, 330.4, 330.4, 313.3, 308.6, 407.5, 333.6, 291.5, 284.2],
    '60 Day Maximum Power 1.0min': [292.9, 292.9, 292.9, 292.9, 261.5, 286.6, 288.7, 291.0, 260.2, 272.7],
    '60 Day Maximum Power 5.0min': [244.6, 244.6, 244.6, 244.6, 235.6, 242.0, 253.9, 253.3, 215.3, 212.1],
    '60 Day Maximum Power 10.0min': [238.9, 238.9, 238.9, 238.9, 231.9, 235.1, 249.2, 247.1, 201.9, 197.2],
    '60 Day Maximum Power 20.0min': [233.6, 233.6, 233.6, 233.6, 229.5, 229.2, 246.1, 240.6, 188.0, 178.5],
    '60 Day Maximum Power 30.0min': [232.9, 232.9, 232.9, 232.9, 226.3, 213.4, 243.7, 237.4, 181.7, 164.5],
    '60 Day Maximum Power 1.0 hr': [145.2, 145.2, 153.9, 153.9, 217.8, 207.9, 198.2, 193.7, 169.4, 151.0],
    '60 Day Maximum Power 1.5 hr': [138.4, 138.6, 152.8, 152.8, 210.2, 193.0, 186.0, 184.8, 167.0, 146.1],
    '60 Day Maximum Power 2.0 hr': [130.1, 130.1, 152.6, 152.6, 185.9, 180.7, 185.1, 174.6, 166.9, 145.4],
    'FTP': [223.2, 223.2, 223.3, 223.3, 224.5, 248.6, 252.2, 252.7, 252.7, 252.7]
})

class TestFtpPredictor(unittest.TestCase):

    def setUp(self):
        self.data = testdata
        self.predictor = FtpPredictor(self.data)

    def test_fit(self, data=None):
        # Test if the fit method runs without errors
        self.predictor.fit(self.data)

    def test_predict(self):
        # Test if the predict method returns the correct number of predictions
        err = 'Number of predicted values did not match number of expected values'
        data = testdata.sample(n=5)
        data = data.drop(['FTP', 'Activity Date'], axis=1)
        data = data.fillna(0)
        self.predictor.fit(self.data)
        predictions = self.predictor.predict(data)
        self.assertEqual(len(predictions), len(data), err)

    def test_predict_values(self):
        # Test if the predict method returns the correct predicted values
        err = 'Predicted values did not match expected values'
        data = testdata.head(3)
        data = data.drop(['FTP', 'Activity Date'], axis=1)
        data = data.fillna(0)
        self.predictor.fit(self.data)
        predictions = self.predictor.predict(data)
        expected_predictions = [225.8, 225.9, 223.9]
        self.assertListEqual(predictions.tolist(), expected_predictions, err)

if __name__ == '__main__':
    unittest.main()