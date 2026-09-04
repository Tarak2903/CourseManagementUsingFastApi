from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.dependency import get_auth_service
from app.schemas.APIResponse import APIResponse
from app.schemas.Auth.Token import Token
from app.services.AuthService import AuthService

router = APIRouter(prefix='/auth')


@router.post("/login", response_model=APIResponse[Token], tags=["Authentication"])
def login_user(form_data: OAuth2PasswordRequestForm = Depends(),
               auth_service: AuthService = Depends(get_auth_service)):

    token = auth_service.login_user(form_data)
    token_response = Token(access_token=token, token_type='bearer')

    return APIResponse(
        success=True,
        message="Login successful",
        data=token_response
    )


# @router.post("/signup")
# def signup_user(user:SignupRequest,auth_service:AuthService=Depends(get_auth_service)):
#     return auth_service.sign_user(user)
