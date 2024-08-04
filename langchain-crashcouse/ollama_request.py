import json


import requests

url = "http://localhost:11434/api/generate"

data = {"model": "gemma2", "prompt": "Why is the sky blue?", "stream": False}

response = requests.post(url, json=data)

if response.status_code == 200:
    text = response.text
    json = json.loads(text)
    print(json["response"])
else:
    print(f"Error: {response.status_code}, Message: {response.text}")
