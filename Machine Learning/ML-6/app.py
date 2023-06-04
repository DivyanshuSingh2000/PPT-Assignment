# app.py - Flask Application
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_loan_eligibility():
    data = request.json
    # Preprocess the input data, if required
    prediction = model.predict(data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
