import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from flask import Flask, render_template
import plotly.graph_objs as go

# Load the dataset
df1 = pd.read_csv("data.csv")
df2= pd.read_csv('data_2genre.csv')

df=df = pd.concat([df1, df2])
df.head()

# Extract the features
X = df.drop("Genre", axis=1)

# Perform unsupervised clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Predict the clusters
labels = kmeans.labels_

# Calculate accuracy
accuracy = np.mean(labels == df["Genre"])

# Flask app initialization
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', accuracy=accuracy)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
