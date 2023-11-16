from config import key
import datetime
import requests

def fetch_data(current_date=None):
    if current_date is None:
        current_date = datetime.date.today()
        url = (f'https://newsapi.org/v2/top-headlines?'
              'sources=al-jazeera-english, bbc-news&'
              'language=en&'
              'from={current_date}&'
              'apiKey=27c93b84409449f8bf127d52b35f0421')
        articles = requests.get(url).json()
        for article in articles['articles']:
            print(article['author'], end='')

fetch_data()