from fastapi import APIRouter
from app.schemas import UserCreate
from app.services import UserService

router=APIRouter()

class UserController:
    def __init__(self,user_service):
        self.user_service=user_service

    @router.post("/users")
    def create_user(self,user):
        self.user_service.add_user(user)

