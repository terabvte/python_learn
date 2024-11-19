import requests
from twilio.rest import Client
MY_LAT = 43.591560 # 43.591560
MY_LON = 10.596240 # 10.596240
API_KEY = "cens"

account_sid = 'AC30988ed6a0c92db892b6525dfb869003'
auth_token = 'a5900bee74dddf95ac7eb8188cc098ba'

# print(message.sid)

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

# print(data["cod"])
# print(data)

w_conditions = []

# w_time = data["list"][0]["dt_txt"]
# w_ID = data["list"][0]["weather"][0]["id"]

for forecast in range(0,4):
    print(data["list"][forecast]["dt_txt"])
    w_conditions.append(data["list"][forecast]["weather"][0]["id"])
    w_conditions.append(data["list"][forecast]["weather"][0]["id"])

for forecast in w_conditions:
    if forecast < 700:
        print("Bring an Umbrella")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
          messaging_service_sid='MG7a38773421f12ecc1f865181176194d8',
          body='Bring an Umbs my man ☔️',
        #   from_="cens"
          to='cens'
        )
        print(message.status)
        break


# print(w_conditions)
