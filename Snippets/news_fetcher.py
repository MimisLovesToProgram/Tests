import requests
import json

# Setting up URL with API key and company names
company_names = {'Microsoft': "MSFT", 'Apple': "AAPL", 'Amazon': "AMZN", 'Facebook': "META", 'Google': "GOOGL"}

"""
url = ('https://newsapi.org/v2/everything?'
       'q=' + ' OR '.join(company_names.keys()) + '&'
       'from=' + 'TWO DAYS FROM TODAY, CHANGE THIS IN PROD' + '&' # Emphasized Item Here
       'to=' + 'TODAY, CHANGE THIS IN PROD AS WELL' + '&' # Here As Well
       'sortBy=publishedAt&'
       'apiKey=YOUR API KEY, DONT FORGET TO CHANGE THIS IN PROD. GET THE KEY WHEN SIGNING UP') # Another One Here.

# Trying to send request to get news
try:
    response = requests.get(url)
except:
    print("Can't access link, please check your internet")
    exit()

news = json.loads(response.text)

# Loop to read new articles, handle the data however you want, by using the tags 'title' or 'description', advisably.
for new in news['articles']:
    print("##############################################################\n")
    print(str(new['title']), "\n\n")
    print('______________________________________________________\n')
    print(str(new['description']), "\n\n") # Also useful when evaluating the headline's positivity. This is basically a brief overview of the article.
    print("..............................................................")
"""

# WAY 2:

import yfinance
import datetime

for company in company_names:
    news = yfinance.Ticker(company_names[company]).news
    for new in news:
        print(new["title"], "Date:", datetime.datetime.fromtimestamp(new["providerPublishTime"]))