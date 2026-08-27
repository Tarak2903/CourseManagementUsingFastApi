from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

class UserRepository:
    def __init__(self,db):
        self.db=db
