from fastapi import APIRouter, Depends

from app.core.dependency import get_mentor_service
from app.core.security import get_current_mentor
from app.models.user import User
from app.services.MentorService import MentorService

router=APIRouter()


@router.post('/mentor/courses',tags=['mentor'])
def add_course(mentor:User=Depends(get_current_mentor),mentor_service:MentorService=Depends(get_mentor_service)):
    print("HEllo world")
