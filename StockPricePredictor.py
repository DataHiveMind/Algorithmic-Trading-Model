import mlflow
import numpy as np
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def __init__(self, experiment_name, tracking_uri):
        self.experiment_name = experiment_name
        self.tracking_uri = tracking_uri
        self.model = None

def train(self, X, y):
    mlflow.set_tracking_uri(self.tracking_uri)
    mlflow.set_experiment(self.experiment_name)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    self.model = LinearRegression()
    self.model.fit(X_train, y_train)

    # Log the model parameters and metrics to MLflow
    with mlflow.start_run():
        mlflow.log_params({"model": "Linear Regression"})
        mlflow.log_metric("train_rmse", self.calculate_rmse(X_train, y_train))
        mlflow.log_metric("test_rmse", self.calculate_rmse(X_test, y_test))
        mlflow.sklearn.log_model(self.model, "model")


def predict(self, X):
    return self.model.predict(X)

def calculate_rmse(self, X, y):
    predictions = self.model.predict(X)
    mse = np.mean((predictions - y) ** 2)
    rmse = np.sqrt(mse)
    return rmse
