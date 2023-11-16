"""
This is file is for fetching data from news API and storing in the database
"""

import requests
from .database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from . import models
import datetime
from .config import key

session = SessionLocal()
models.Base.metadata.create_all(bind=engine)


def fetch_data(current_date=None):
       if current_date is None:
              current_date = datetime.date.today()
       url = (f'https://newsapi.org/v2/top-headlines?'
              'sources=al-jazeera-english, bbc-news&'
              'language=en&'
              'from={current_date}&'
              'apiKey={key}')


       articles = requests.get(url).json()
       for article_data in articles['articles']:
              article = models.Article(
                     author = article_data['author'],
                     title = article_data['title'],
                     description = article_data['description'],
                     url_to_image = article_data['urlToImage'],
                     content = article_data['content'],
                     source_url = article_data['url']
              )
              session.add(article)
       session.commit()


def check_and_fetch_data(db: Session):
    # Check if articles table is empty
    if db.query(models.Article).first() is None:
       # If empty, fetch data
       fetch_data()
    else:
       # If not empty, delete all records
       db.query(models.Article).delete()
       db.commit()
       # Fetch data
       fetch_data()

if __name__ == '__main__':
       db = SessionLocal()
       check_and_fetch_data(db)
