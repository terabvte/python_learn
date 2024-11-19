import requests
from datetime import datetime

NUT_APP_ID = "de12f083"
NUT_API_KEY = "8cfb569db17469b56f9e0a80a0887f82"

nut_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nut_header = {
    "x-app-id": NUT_APP_ID,
    "x-app-key": NUT_API_KEY
}

query = input("Tell me which exercises you did: ")

nut_parameters = {
    "query": query,
    "weight_kg": 88.3,
    "height_cm": 170,
    "age": 20
}

response = requests.post(url=nut_endpoint, headers=nut_header, json=nut_parameters)
response = response.json()
# print(response.text)
print(response)

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

entry = [date, time, response["exercises"][0]["name"].title(), response["exercises"][0]["duration_min"], response["exercises"][0]["nf_calories"]]

print(entry)
