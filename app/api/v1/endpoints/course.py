from fastapi import APIRouter, Depends

from app.core.dependency import get_course_service, get_intern_service
from app.core.security import get_current_mentor, get_current_intern
from app.models.user import User
from app.schemas.Course.CourseCreationRequest import CourseCreationRequest
from app.services.CourseService import CourseService
from app.services.InternService import InternService

router=APIRouter()


@router.post('/courses',tags=['Mentor'])
async def add_course(course:CourseCreationRequest,mentor:User=Depends(get_current_mentor),
               course_service:CourseService=Depends(get_course_service)):
    course_service.add_course(course)

# @router.get("/courses",tags=['Intern'])
# async def get_courses_intern(current_user:User=Depends(get_current_intern),intern_service:InternService=Depends(get_intern_service)):
#     return intern_service.get_course(current_user)

@router.get("/courses",tags=['Mentor'])
async def get_courses_mentor(course_service:CourseService=Depends(get_course_service)
                             ,current_mentor:User=Depends(get_current_mentor)):
    return course_service.get_mentor_courses()

