import requests
import pandas
import json

response = requests.get("http://127.0.0.1:8000/data")
data = response.json()


print(data[0])