import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/fraud_detector.pkl')

# Load the data to predict on
df = pd.read_csv('data/processed.csv')  # You can replace this with new data later

# Select features
X = df[['value', 'gas', 'gasPrice', 'fee']]

# Make predictions
df['anomaly'] = model.predict(X)
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})  # 0 = normal, 1 = fraud

# Show suspicious transactions
suspicious = df[df['anomaly'] == 1]

print("🔍 Suspicious Transactions Detected:")
print(suspicious)

# Optional: Save them to a file
suspicious.to_csv('data/suspicious_tx.csv', index=False)
