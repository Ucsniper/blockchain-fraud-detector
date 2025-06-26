from web3 import Web3
import requests
import time

# Connect to Ethereum via Infura
INFURA_URL = 'https://mainnet.infura.io/v3/b073c76c679f4d989d4c60b3b77c966f'
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def send_to_api(tx):
    # Calculate features
    value = float(tx['value']) / 1e18
    gas = tx['gas']
    gas_price = float(tx['gasPrice']) / 1e9
    fee = gas * gas_price

    payload = {
        "value": value,
        "gas": gas,
        "gasPrice": gas_price,
        "fee": fee
    }

    # Send to Flask API
    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=payload)
        result = response.json()
        if result['anomaly']:
            print(f"🚨 Suspicious Transaction Detected! {tx['hash'].hex()}")
            print(payload)
    except Exception as e:
        print("❌ API error:", e)

def monitor_blocks():
    print("🔁 Starting live transaction monitor...")
    latest = web3.eth.block_number

    while True:
        block = web3.eth.get_block(latest, full_transactions=True)
        print(f"\n🧱 New Block {latest} with {len(block.transactions)} txs")

        for tx in block.transactions:
            send_to_api(tx)

        latest += 1
        time.sleep(12)  # Ethereum ~12s per block

if __name__ == "__main__":
    monitor_blocks()
