import requests
import logging

# Define the URL of your Flask app's endpoint
url = 'http://127.0.0.1:5000/predict'  # Replace with your app's URL

# Define the JSON payload
payload = {
    "CHAS": {
        "0": 0
    },
    "RM": {
        "0": 6.575
    },
    "TAX": {
        "0": 296.0
    },
    "PTRATIO": {
        "0": 15.3
    },
    "B": {
        "0": 396.9
    },
    "LSTAT": {
        "0": 4.98
    }
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
if response.status_code == 200:
    print("Prediction:", response.json()["prediction"])
else:
    print("Error:", response.status_code, response.text)
