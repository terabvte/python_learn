import requests
from datetime import datetime

def date_converter(date):
    date = date.split(" ")
    date.pop()
    date = date[0]
    date = date.replace("-", "")
    return date

today = str(datetime.now())
today = date_converter(today)

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "terabvte"
TOKEN = ""

pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Piano Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "kuro",
}

headers = {"X-USER-TOKEN": TOKEN}
# requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)

graph_ID = "graph1"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_ID}"
# print(pixel_endpoint)
pixel_parameters = {
    "date": today,
    "quantity": "30"
}


print(today)

# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
update_endpoint = pixel_endpoint + today
response = requests.put(url=update_endpoint, json=pixel_parameters, headers=headers)
print(response.text)
