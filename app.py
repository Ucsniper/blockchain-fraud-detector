<<<<<<< HEAD
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('models/fraud_detector.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define expected input fields
FEATURES = ['value', 'gas', 'gasPrice', 'fee']

@app.route('/')
def home():
    return "🚀 Blockchain Fraud Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Ensure all required fields are present
    if not all(feature in data for feature in FEATURES):
        return jsonify({'error': f'Missing one or more required fields: {FEATURES}'}), 400

    # Prepare input for model
    X = pd.DataFrame([{
        'value': data['value'],
        'gas': data['gas'],
        'gasPrice': data['gasPrice'],
        'fee': data['fee']
    }])

    # Predict using Isolation Forest
    prediction = model.predict(X)[0]
    is_anomaly = True if prediction == -1 else False

    return jsonify({'anomaly': is_anomaly})

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('models/fraud_detector.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define expected input fields
FEATURES = ['value', 'gas', 'gasPrice', 'fee']

@app.route('/')
def home():
    return "🚀 Blockchain Fraud Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Ensure all required fields are present
    if not all(feature in data for feature in FEATURES):
        return jsonify({'error': f'Missing one or more required fields: {FEATURES}'}), 400

    # Prepare input for model
    X = pd.DataFrame([{
        'value': data['value'],
        'gas': data['gas'],
        'gasPrice': data['gasPrice'],
        'fee': data['fee']
    }])

    # Predict using Isolation Forest
    prediction = model.predict(X)[0]
    is_anomaly = True if prediction == -1 else False

    return jsonify({'anomaly': is_anomaly})

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 8272e736669d73bee04ec8450303df87659d9afc
