from fastapi import APIRouter, Depends

from app.core.dependency import  get_intern_service
from app.core.security import get_current_mentor
from app.models.user import User
from app.schemas.Intern.InternCreationRequest import InternCreationRequest
from app.services.InternService import InternService

router=APIRouter()



@router.post('/interns',tags=['Mentor'])
def add_intern(intern:InternCreationRequest,
               intern_service:InternService=Depends(get_intern_service),
               mentor:User=Depends(get_current_mentor)):
    intern_service.add_intern(intern,mentor.id)

