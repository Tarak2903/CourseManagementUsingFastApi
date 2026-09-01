from fastapi import APIRouter, Depends

from app.core.security import get_current_mentor
from app.models.user import User

router=APIRouter()


@router.post('/mentor/courses',tags=['mentor'])
def add_course(mentor:User=Depends(get_current_mentor)):
    pass