from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.AuthRepository import AuthRepository
from app.repositories.UserRepository import UserRepository
from app.core.database import get_db
from app.services.AuthService import AuthService
from app.services.UserService import UserService

def get_user_repository(db:Session=Depends(get_db)):
    return UserRepository(db)

def get_user_service(user_repo:UserRepository=Depends(get_user_repository)):
    return UserService(user_repo)


def get_auth_repository(db:Session=Depends(get_db)):
    return AuthRepository(db)

def get_auth_service(auth_repo:AuthRepository=Depends(get_auth_repository)):
    return AuthService(auth_repo)