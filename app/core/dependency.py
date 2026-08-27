from fastapi import Depends
from sqlalchemy.orm import Session
from app.repositories.UserRepository import UserRepository
from app.core.database import get_db
from app.services.UserService import UserService

def get_user_repository(db:Session=Depends(get_db)):
    return UserRepository(db)

def get_user_service(user_repo:UserRepository=Depends(get_user_repository)):
    return UserService(user_repo)