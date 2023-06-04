from flask import Flask, render_template
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.sql.functions import col, mean, isnan, when
from pyspark.sql.types import DoubleType

import plotly.graph_objects as go

# Create a Flask app
app = Flask(__name__)

# Define the route for displaying the predictions
@app.route('/')
def display_predictions():
    SparkSession.builder.appName("ChemicalClassification").getOrCreate()

    data = spark.read.csv("/content/drive/MyDrive/Colab Notebooks/ML/indian_liver_patient.csv", header=True, inferSchema=True)


    # Calculate the mean of each column with missing values
    mean_values = data.select(*(mean(col(c)).alias(c) for c in data.columns if data.select(col(c)).filter(col(c).isNull()).count() > 0)).collect()[0].asDict()

    # Fill missing values with the corresponding mean
    filled_data = data
    for column, mean_value in mean_values.items():
        filled_data = filled_data.withColumn(column, when(col(column).isNull(), mean_value).otherwise(col(column)))

    # Replace infinite values with null for all features
    for feature in filled_data.columns:
        filled_data = filled_data.withColumn(feature, when(~isnan(col(feature)), col(feature)).otherwise(None))


    # Convert the "Gender" column to numerical using StringIndexer
    gender_indexer = StringIndexer(inputCol="Gender", outputCol="GenderIndex")
    filled_data = gender_indexer.fit(filled_data).transform(filled_data)

    # Assemble the features into a vector
    feature_columns = ["Age", "Total_Bilirubin", "Direct_Bilirubin", "Alkaline_Phosphotase",
                    "Alamine_Aminotransferase", "Aspartate_Aminotransferase", "Total_Protiens",
                    "Albumin", "Albumin_and_Globulin_Ratio", "GenderIndex"]
    assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
    data = assembler.transform(filled_data)

    # Select only the necessary columns for model training
    data = data.select("features", "Dataset")

    # Split the data into train and test sets
    train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)

    # Create an instance of the LogisticRegression model
    logreg = LogisticRegression(labelCol="Dataset")

    # Fit the model to the train data
    model = logreg.fit(train_data)

    # Make predictions on the test data
    predictions = model.transform(test_data)

    # Show the predicted labels and corresponding features
    predictions.select("prediction", "features").show()

    # Create a Plotly bar chart of the predictions
    fig = go.Figure(data=go.Bar(x=predictions['features'], y=predictions['prediction']))

    # Render the HTML template with the predicted values and plot
    return render_template('predictions.html', predicted_values=predictions['prediction'], plot=fig.to_html())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
