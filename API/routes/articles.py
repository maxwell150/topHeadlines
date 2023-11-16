from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db, engine
from .. import models



router = APIRouter(
    tags=['Articles'],
    prefix='/articles'
)


@router.get("/")
async def get_articles(db: Session=Depends(get_db)):
    articles = db.query(models.Article).order_by(models.Article.id.desc()).all()
    return articles

@router.get("/apiKey={apikey}")
async def get_articles(apikey: str, db: Session=Depends(get_db)):
    api_key = db.query(models.API_KEY).filter(models.API_KEY.key == apikey).first()
    if not api_key:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Api Key needed')
    articles = db.query(models.Article).order_by(models.Article.id.desc()).all()
    return articles

@router.get('/latest')
def get_one_article(db: Session=Depends(get_db)):
    latest = db.query(models.Article).first()
    return latest

    print(latest)