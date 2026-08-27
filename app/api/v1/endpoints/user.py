from fastapi import APIRouter, Depends

from app.core.dependency import get_user_service
from app.schemas.UserCreate import UserCreate
from app.services.UserService import UserService

router=APIRouter()


@router.post("/users")
def create_user(user:UserCreate,user_service:UserService=Depends(get_user_service)):
    user_service.add_user(user)
