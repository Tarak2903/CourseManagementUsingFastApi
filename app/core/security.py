from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
import jwt

from app.core.config import settings
from app.core.dependency import get_user_repository
from app.exceptions.UnAuthorizedException import UnAuthorizedException
from app.repositories.UserRepository import UserRepository
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/users/login')

async def get_current_user(token:str=Depends(oauth2_scheme),user_repo:UserRepository=Depends(get_user_repository)):
    try:
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        username=payload.get('user_name')
        if username is None:
            raise UnAuthorizedException
        user =user_repo.check_user_name_exists(username)
        return user

    except InvalidTokenError:
        raise UnAuthorizedException("Could not validate the credentials")