import requests

# response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
# response_iss.raise_for_status()
# data_iss = response_iss.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# print(f"The latitude is: {latitude}")
# print(f"The longitude is: {longitude}")

parameters = {
    "lat": 43.591560,
    "lng": 10.596240,
    "formatted": 0
}

response_pos = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_pos.raise_for_status()
data_pos = response_pos.json()
# print(data_pos)

sunrise = data_pos["results"]["sunrise"]
sunset = data_pos["results"]["sunset"]

print(f"The sunrise is: {sunrise}")
print(f"The sunset is: {sunset}")
