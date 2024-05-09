

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd

class FtpPredictor:
    def __init__(self, filename=None):
        """
        Initialize the FtpPredictor class.

        Parameters:
        - filename (str): The name of the file to be used for training the prediction model. 
        """

        if filename is None:
            filename = 'data/extended_activities_with_ftp.csv' # default filename
        
        self.filename = filename
        self.model = None

    def fit(self, data=None):
        """
        Fit the model to the training data.

        Parameters:
        - data (DataFrame or str): The DataFrame or filename to be used for training the model.
        """

        # Load the training data
        if data is None:
            data = pd.read_csv(self.filename)
        elif isinstance(data, str):
            data = pd.read_csv(data)
        # If data is already a DataFrame, it will be used directly

        # Clean the training data
        data = data.dropna(subset=['FTP'])
        data = data.drop(['Activity Date'], axis=1)
        data = data.fillna(0)

        X = data.drop('FTP', axis=1)  # Features
        y = data['FTP']               # Target variable

        # Split the data into training and testing sets
        #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a Linear Regression model
        self.model = RandomForestRegressor(random_state=42)
        #self.model.fit(X_train, y_train)
        self.model.fit(X, y)

    def predict(self, data):
        """
        Make predictions using the trained model.

        Parameters:
        - record (dataframe): The dataframe to be used for making predictions.

        Returns:
        - ftp (int): The predicted value for the given record.
        """

        if self.model is None:
            self.fit()

        # return 0 for each record in data
        ftp_pred = self.model.predict(data)

        return np.around(ftp_pred, decimals=1)
