import pandas as pd
import json

# Load Ethereum transaction data from JSON
with open('data/eth_tx.json') as f:
    tx_data = json.load(f)

# Convert to pandas DataFrame
df = pd.DataFrame(tx_data)

# Basic cleaning: Remove missing or incomplete data
df.dropna(inplace=True)

# Convert all values to numeric (they're already converted in fetch_data.py)
df['value'] = df['value'].astype(float)
df['gas'] = df['gas'].astype(int)
df['gasPrice'] = df['gasPrice'].astype(float)

# Add a new feature: transaction fee (gas × gasPrice)
df['fee'] = df['gas'] * df['gasPrice']

# Add another feature: whether it’s a high-value transaction (arbitrary threshold)
df['high_value'] = df['value'] > 10  # True/False

# Select only useful features for ML
features_df = df[['value', 'gas', 'gasPrice', 'fee']]

# Save cleaned features to CSV for model training
features_df.to_csv('data/processed.csv', index=False)

print("✅ Data preprocessed and saved to data/processed.csv")
