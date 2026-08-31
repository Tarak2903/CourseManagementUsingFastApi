
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.dependency import get_user_service
from app.schemas.Token import Token
from app.schemas.UserCreate import UserCreate
from app.services.UserService import UserService
from app.core.security import get_current_user
from app.models.user import User
router=APIRouter()


@router.post("/users")
def create_user(user:UserCreate,user_service:UserService=Depends(get_user_service)):
    user_service.add_user(user)

@router.post("/users/login",response_model=Token)
def login_user(form_data:OAuth2PasswordRequestForm=Depends(),
    user_service:UserService=Depends(get_user_service)):

    token=user_service.login_user(form_data)
    return Token(access_token=token,token_type='bearer')

@router.get("/users/courses")
def get_courses(current_user:User=Depends(get_current_user)):
    return current_user

