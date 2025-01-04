import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
ACC_SID = os.getenv("ACC_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
PHONE_NO =os.environ.get("PHONE_NO")



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


news_params = {
    'apiKey': NEWS_API_KEY,
    'qInTitle': COMPANY_NAME
}
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

yesterday = float(yesterday_closing_price)
day_before_yesterday = float(day_before_yesterday_closing_price)
difference = yesterday - day_before_yesterday
up_or_down = "⃤⃤ " if difference > 0 else "▽"

percentage_diff = round((difference / yesterday) * 100)

if abs(percentage_diff) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:2]
    formatted_article = [
        f"{STOCK_NAME}:{up_or_down} {difference}%\nHeadline: {article['title']}\n Content: {article['description']}"
        for article in three_articles
    ]

    client = Client(ACC_SID, AUTH_TOKEN)
    for art in formatted_article:
        message = client.messages.create(
            from_='+16504762756',
            to=f'{PHONE_NO}',
            body=art
        )
        print(message.sid)
