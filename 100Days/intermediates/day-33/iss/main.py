import requests
import smtplib
from datetime import datetime
import time

GOOGLE_APP_PW = "Censored"
my_email = "marcofediuc@gmail.com"

MY_LAT = 43.591560  # Your latitude
MY_LONG = 10.596240  # Your longitude


def sixty_to_deca(hr, min):
    return round(min / 60 + hr, 2)


def is_iss_close():
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
    else:
        return False


def is_dark():
    if time_now_DEC > sunset_DEC and time_now_DEC < sunrise_DEC:
        return True
    else:
        return False


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

sunrise_minute = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
sunset_minute = int(data["results"]["sunset"].split("T")[1].split(":")[1])

sunrise_HM = str(sunrise_hour) + ":" + str(sunrise_minute)
# sunrise_DEC = round(sunrise_minute / 60 + sunrise_hour, 2)
sunrise_DEC = sixty_to_deca(sunrise_hour, sunrise_minute)

sunset_HM = str(sunset_hour) + ":" + str(sunset_minute)
sunset_DEC = sixty_to_deca(sunset_hour, sunset_minute)

# print(f"Sunrise: {sunrise_HM}")
# print(f"Sunrise: {sunrise_DEC}")

# print(f"Sunset: {sunset_HM}")
# print(f"Sunset: {sunset_DEC}")

time_now = datetime.now()
my_hour = time_now.hour
my_minute = time_now.minute

time_now_HM = str(my_hour) + ":" + str(my_minute)
time_now_DEC = sixty_to_deca(my_hour, my_minute)

# print(f"My time: {time_now_HM}")
# print(f"My time: {time_now_DEC}")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    print(time.ctime())
    if is_dark() and is_iss_close():
        print(f"It is currently {time_now_HM}")
        print(f"The iss is currently at LAT: {iss_latitude} LONG: {iss_longitude}")
        print(f"Location to be checked is LAT: {MY_LAT} LONG: {MY_LONG}")
        print(f"The two conditions for the ISS appearance are met:")
        print("1. Dark")
        print("2. ISS is within 5 degrees of home latitude and longitude")
        print("Sending email...")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=GOOGLE_APP_PW)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="marcofediuc04@gmail.com",
                msg="Subject:THE ISS IS ABOVE YOU!\n\nLook up right now!!!",
            )
        print("Email sent successfully!")

    else:
        print("damn... not yet :(")

    time.sleep(60)
