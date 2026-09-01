from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
import jwt

from app.core.config import settings
from app.core.dependency import  get_auth_repository
from app.core.enums import Role
from app.exceptions.UnauthenticatedException import UnauthenticatedException
from app.exceptions.ForbiddenException import ForbiddenException
from app.repositories.AuthRepository import AuthRepository
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/auth/login')

async def get_current_intern(token:str=Depends(oauth2_scheme),auth_repo:AuthRepository=Depends(get_auth_repository)):
    try:
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        username=payload.get('user_name')
        if username is None:
            raise UnauthenticatedException
        user =auth_repo.find_user_by_username(username)
        return user

    except InvalidTokenError:
        raise UnauthenticatedException("Could not validate the credentials")



async def get_current_mentor(token:str=Depends(oauth2_scheme),auth_repo:AuthRepository=Depends(get_auth_repository)):
    try:
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        username=payload.get('user_name')
        if username is None:
            raise UnauthenticatedException("User not authenticated")
        user=auth_repo.find_user_by_username(username)
        if user.role is not Role.MENTOR:
            raise ForbiddenException("User doesnt have the permission to perform the following actions")
        return user
    except InvalidTokenError:
        raise UnauthenticatedException("Could not validate the credentials")