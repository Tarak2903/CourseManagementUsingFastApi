from fastapi import APIRouter
from app.schemas.UserCreate import UserCreate
router=APIRouter()


@router.post("/mentors")
def create_mentor(user:UserCreate):
    pass
