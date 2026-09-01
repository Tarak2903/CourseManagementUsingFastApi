from datetime import datetime, timezone, timedelta

import jwt
from pwdlib import PasswordHash

from app.core.config import settings
from app.exceptions.UnauthenticatedException import UnAuthorizedException
from app.exceptions.user_exceptions import UserAlreadyExistsException, UserDoesntExistsException
from app.schemas.Auth.SignupRequest import SignupRequest


class AuthService:
    def __init__(self,auth_repo):
        self.auth_repo=auth_repo
        self.password_hash=PasswordHash.recommended()

    @staticmethod
    def create_token(payload:dict):
        token= jwt.encode(payload,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
        print(token)
        return token

    def add_user(self,user:SignupRequest):
        hashed_password=self.password_hash.hash(user.password)
        user.password=hashed_password
        if self.auth_repo.find_user_by_username(user.user_name) is not None:
            raise UserAlreadyExistsException("User already exists")
        self.auth_repo.add_user(user)

    def login_user(self, user):
        user_info = self.auth_repo.find_user_by_username(user.username)
        if user_info is None:
            raise UserDoesntExistsException("User doesnt exists")
        if not self.password_hash.verify(user.password, user_info.password):
            raise UnAuthorizedException("User not authorized")
        return self.create_token(
            {"user_name": user.username,
             "exp": datetime.now(timezone.utc) + timedelta(minutes=15)})