from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.dependency import get_auth_service
from app.schemas.Auth.SignupRequest import SignupRequest
from app.schemas.Auth.Token import Token
from app.services.AuthService import AuthService

router=APIRouter(prefix='/auth')


@router.post("/login",response_model=Token,tags=["Authentication"])
def login_user(form_data:OAuth2PasswordRequestForm=Depends(),
    auth_service:AuthService=Depends(get_auth_service)):

    token=auth_service.login_user(form_data)
    return Token(access_token=token,token_type='bearer')

@router.post('/signup',tags=["Authentication"])
def create_user(user:SignupRequest,auth_service:AuthService=Depends(get_auth_service)):
    auth_service.add_user(user)

