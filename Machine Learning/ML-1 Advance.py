import dask.dataframe as dd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset
df = dd.read_csv("FacebookRecruiting/train.csv")

# Preprocess the data
X = df[['source_node', 'destination_node']]
y = df[['acceptance_label']] 

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start an MLflow run
mlflow.set_experiment("FriendRequestPrediction")
with mlflow.start_run():
    # Train the model
    model = LogisticRegression()
    model.fit(X_train.compute(), y_train.compute())
    
    # Evaluate the model
    accuracy = model.score(X_test.compute(), y_test.compute())

    # Log the model parameters and evaluation metric
    mlflow.log_params(model.get_params())
    mlflow.log_metric("accuracy", accuracy)
    
    # Save the trained model
    mlflow.sklearn.log_model(model, "model")
