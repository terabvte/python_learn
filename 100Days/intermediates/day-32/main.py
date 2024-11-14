# SMTP emails and such..
import smtplib
import random
# GOOGLE_APP_PW = "embbyplbjzyiqaep"  # embb yplb jzyi qaep
# my_email = "marcofediuc@gmail.com"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=GOOGLE_APP_PW)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="marcofediuc04@gmail.com",
#         msg="Subject:Wassuz\n\nAre you fine?"
#     )

import datetime as dt

now = dt.datetime.now()
wd = now.weekday()

with open("./100Days/intermediates/day-32/quotes.txt") as quote:
    quotes = [line.rstrip() for line in quote]

print(random.choice(quotes))

# print(wd)
