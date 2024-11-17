import requests
MY_LAT = 43.591560
MY_LON = 10.596240
API_KEY = "0f3f21e452f8073b8ca75787534afc07"

# http://api.openweathermap.org/data/2.5/weather?lat=43.591560&lon=10.596240&appid=0f3f21e452f8073b8ca75787534afc07

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

print(data["cod"])
print(data)
