import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "value": 0.5,
    "gas": 21000,
    "gasPrice": 50.0,
    "fee": 1050000.0
}

response = requests.post(url, json=data)
print(response.json())
