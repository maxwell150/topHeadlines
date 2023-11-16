import secrets
from ..database import get_db
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models

router = APIRouter(
    tags=['APIKEY']
)


def generate_api_key():
    return secrets.token_urlsafe(32)



@router.get("/generate_api_key")
def api_key(db: Session = Depends(get_db)):
    key = generate_api_key()
    new_key = models.API_KEY(key)
    db.add(new_key)
    db.commit()
    return {"api_key": key}

