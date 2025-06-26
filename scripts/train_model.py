import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# Load the processed data
df = pd.read_csv('data/processed.csv')

# Train on selected features
X = df[['value', 'gas', 'gasPrice', 'fee']]

# Define and train Isolation Forest
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
model.fit(X)

# Predict anomalies (-1 = anomaly, 1 = normal)
df['anomaly'] = model.predict(X)
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})  # 0 = normal, 1 = fraud/anomaly

# Save the labeled data to CSV
df.to_csv('data/labeled.csv', index=False)

# Save the trained model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/fraud_detector.pkl')

print("✅ Model trained and saved to models/fraud_detector.pkl")
print("📄 Labeled transactions saved to data/labeled.csv")
