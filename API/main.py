"""
This main file is responsible for tying all the module together. 
"""
from fastapi import FastAPI
from .config import host, password, database_name, user
import pymysql
from . import models
from fastapi.middleware.cors import CORSMiddleware
from .routes import apikey, articles
from .database import engine, SessionLocal
from .fetchdata import fetch_data


models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

check_and_fetch_data(db)


app = FastAPI()

app.include_router(apikey.router)
app.include_router(articles.router)

# allowing Cross-Origin Resource Sharing between this API and the React Application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["get"],
    allow_headers=["*"],
)



def test_db():
    try:
        con = pymysql.connect(host=host, user=user,passwd=password, database=database_name)
        cur = con.cursor()
        print("Database connection was successfull")
    except Exception as err:
        print("Database connnection failed")
        print("error: ", err)
test_db()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    test_db()
