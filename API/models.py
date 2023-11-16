"""This file defines models for the database"""

from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, DateTime, Integer, String, ForeignKey, Text
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('now()'))
    
class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    author = Column(String(255))
    title = Column(String(255))
    description = Column(Text)
    url_to_image = Column(String(255))
    content = Column(Text)
    source_url = Column(Text)

class API_KEY(Base):
    __tablename__ = 'apikeys'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    key = Column(String(255), unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,
                        server_default=text('now()'))
    def __init__(self, key):
        self.key = key



    