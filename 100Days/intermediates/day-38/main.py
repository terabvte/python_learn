import requests
from datetime import datetime

NUT_APP_ID = "cens"
NUT_API_KEY = "cens"

nut_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nut_header = {
    "x-app-id": NUT_APP_ID,
    "x-app-key": NUT_API_KEY
}

query = input("Tell me which exercises you did: ")

nut_parameters = {
    "query": query,
}

nut_response = requests.post(url=nut_endpoint, headers=nut_header, json=nut_parameters)
nut_response = nut_response.json()
# print(response.text)
# print(nut_response)

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

entry = [date, time, nut_response["exercises"][0]["name"].title(), nut_response["exercises"][0]["duration_min"], nut_response["exercises"][0]["nf_calories"]]

print(entry)


sheety_endpoint = "cens"
sheety_parameters = {
    "workout": {
        "date": entry[0],
        "time": entry[1],
        "exercise": entry[2],
        "duration": entry[3],
        "calories": entry[4],
    }
}

sheety_request = requests.post(url=sheety_endpoint, json=sheety_parameters)
print(sheety_request.text)
sheety_request.raise_for_status()
