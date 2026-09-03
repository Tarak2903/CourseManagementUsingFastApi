
from fastapi import APIRouter, Depends

from app.core.dependency import get_intern_service
from app.core.security import get_current_mentor, get_current_intern
from app.models.user import User
from app.schemas.Intern.InternPasswordRequest import InternPasswordRequest
from app.services.InternService import InternService

router=APIRouter()

@router.get("/interns",tags=['Mentor'])
def get_interns_by_mentor_id(intern_service:InternService=Depends(get_intern_service),mentor:User=Depends(get_current_mentor)):
    return intern_service.get_interns_by_mentor_id(mentor.id)


# @router.get("/interns/courses/{intern_id}",tags=['Intern'])
# def get_course_detail(intern_id,current_user:User=Depends(get_current_intern),intern_service:InternService=Depends(get_intern_service)):
#     return intern_service.get_course_by_id(intern_id,current_user)


@router.put("/interns",tags=['Intern'])
def change_intern_password(password_req:InternPasswordRequest,intern_service:InternService=Depends(get_intern_service)
                           ,intern:User=Depends(get_current_intern)):
    return intern_service.change_intern_password(intern.id,password_req)
