import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "9BONCDX6E5RG5VSB"
NEWS_API_KEY = "749c286be7db430f98edf293451d0091"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_url = 'https://www.alphavantage.co/query'
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
stock_r = requests.get(url=stock_url, params=stock_parameters)
stock_data = stock_r.json()
yest_close = float(stock_data["Time Series (Daily)"]["2024-11-15"]["4. close"])
two_yest_close = float(stock_data["Time Series (Daily)"]["2024-11-14"]["4. close"])

print(f"Yesterday TSLA closed at: {yest_close}")
print(f"The day before yesterday TSLA closed at: {two_yest_close}")

delta = round(((yest_close - two_yest_close) / two_yest_close) * 100, 2)
print(f"{delta}%")
if delta >= 5 or delta <= -5:
    print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_url = "https://newsapi.org/v2/top-headlines"
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": "Tesla",
    "pageSize" : 3,
}
news_r = requests.get(url=news_url, params=news_parameters)
news_data = news_r.json()

print(news_data)

last_3_headlines = []
last_3_briefs = []

for i in range(0,3):
    last_3_headlines.append(news_data["articles"][i]["title"])
    last_3_briefs.append(news_data["articles"][i]["content"])

# print(last_3_headlines)
# print(last_3_briefs)

for i in range(0,3):
    print(f"TSLA: 🔺{delta}\nHeadline: {last_3_headlines[i]}\nBrief: {last_3_briefs[i]}")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
