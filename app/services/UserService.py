from datetime import datetime, timedelta, timezone
import jwt
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from app.exceptions.UnAuthorizedException import UnAuthorizedException
from app.exceptions.user_exceptions import UserAlreadyExistsException, UserDoesntExistsException
from app.repositories.UserRepository import UserRepository
from app.schemas.UserLogin import UserLogin
from app.core.config import settings
class UserService:
    def __init__(self,user_repo:UserRepository):
        self.user_repo=user_repo
        self.password_hash=PasswordHash.recommended()
        self.oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

    @staticmethod
    def create_token(payload:dict):
        token= jwt.encode(payload,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
        print(token)
        return token

    def add_user(self,user):
        hashed_password=self.password_hash.hash(user.password)
        user.password=hashed_password
        if self.user_repo.check_user_name_exists(user.user_name) is None:
            raise UserAlreadyExistsException("User already exists")
        self.user_repo.add_user(user)


    def login_user(self,user):
        user_info=self.user_repo.check_user_name_exists(user.username)
        if self.user_repo.check_user_name_exists(user.username) is None:
            raise UserDoesntExistsException("User doesnt exists")
        if not self.password_hash.verify(user.password,user_info.password):
            raise UnAuthorizedException("User not authorized")
        return self.create_token(
            {"user_name" : user.username,
             "exp" :datetime.now(timezone.utc)+timedelta(minutes=15)})



