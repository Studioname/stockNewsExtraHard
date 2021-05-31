import datetime as dt
import requests
import os
from twilio.rest import Client

#your telephone goes here

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
av_api_key = os.environ["AV_API_KEY"]
news_api_key = os.environ["NEWS_API_KEY"]
auth_token = os.environ["AUTH_TOKEN"]
my_telephone = os.environ["MY_TELEPHONE"]
account_sid = os.environ["ACCOUNT_SID"]

news_url = "https://newsapi.org/v2/everything"
av_url = "https://www.alphavantage.co/query"

client = Client(account_sid, auth_token)


def get_previous_date(number_of_days_ago):
    days = dt.datetime.now() - dt.timedelta(days=number_of_days_ago)
    return days.strftime("%Y-%m-%d")


news_website_parameters = {
    "q" : "Tesla",
    "from" : get_previous_date(1),
    "sortBy" : "popularity",
    "apiKey" : news_api_key
}

av_parameters = {
    "function" : "GLOBAL_QUOTE",
    "symbol" : STOCK,
    "apikey" : av_api_key
}


def send_alert():

    for article in articles:

        message = client.messages \
                        .create(
                             body=f"""{STOCK}{symbol}\n{article['title']}\n{article['description']}
                             """,
                             from_='+13127560470',
                             to=my_telephone
                         )

        print(message.sid)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=av_url,params=av_parameters)
data = response.json()
change = data['Global Quote']['10. change percent']

#change is a string expressing a float as percentage. We remove the % sign and convert to float [floats can still be - number]

change = float(change[:-2])

#news api stuff

news_response = requests.get(url=news_url, params=news_website_parameters)
news_data = news_response.json()
articles = news_data['articles'][0:3]

if change >= 5:
    symbol = f"🔺{round(change,2)}%"
    send_alert()
elif change <= -5:
    symbol = f"🔻{round(change,2)}%"
    send_alert()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


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