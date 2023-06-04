import dask.dataframe as dd
from dask_ml.model_selection import train_test_split
from dask_ml.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
from flask import Flask, render_template
import plotly.graph_objs as go
import pandas as pd

# Load the dataset into a Dask DataFrame
df = dd.read_csv("advertising.csv")

# Split the dataset into features and target variable
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert Dask DataFrames to Dask Arrays
X_train_array = X_train.to_dask_array(lengths=True)
y_train_array = y_train.to_dask_array(lengths=True)

# Create an instance of the LinearRegression estimator
regressor = LinearRegression()

# Train the model
regressor.fit(X_train_array, y_train_array)

# Evaluate the model on the test set
X_test_array = X_test.to_dask_array(lengths=True)
y_test_array = y_test.to_dask_array(lengths=True)
score = regressor.score(X_test_array, y_test_array)

# Calculate predicted profit based on marketing spending
marketing_spending = [[100, 50, 25]]  # Example: Spending $100 on TV, $50 on Radio, $25 on Newspaper
predicted_profit = regressor.predict(marketing_spending)

# Flask app initialization
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', predicted_profit=predicted_profit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
