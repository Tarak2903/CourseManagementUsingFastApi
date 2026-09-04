from fastapi import APIRouter, Depends

from app.core.dependency import get_course_service
from app.core.security import get_current_mentor
from app.models.user import User
from app.schemas.APIResponse import APIResponse
from app.schemas.Course.CourseCreationRequest import CourseCreationRequest
from app.schemas.Course.CourseListResponse import CourseListResponse
from app.schemas.Course.CourseResponse import CourseResponse
from app.services.CourseService import CourseService

router = APIRouter()


@router.post('/courses', response_model=APIResponse[CourseResponse], tags=['Mentor'])
async def add_course(course: CourseCreationRequest,
                      mentor: User = Depends(get_current_mentor),
                      course_service: CourseService = Depends(get_course_service)):

    course_service.add_course(course)

    return APIResponse(
        success=True,
        message="Course created successfully",
        data=CourseResponse(
            course_name=course.name,
            total_sections=course.total_section,
            course_code=course.course_code
        )
    )


# @router.get("/courses",tags=['Intern'])
# async def get_courses_intern(current_user:User=Depends(get_current_intern),intern_service:InternService=Depends(get_intern_service)):
#     return intern_service.get_course(current_user)

@router.get("/courses", response_model=APIResponse[CourseListResponse], tags=['Mentor'])
async def get_courses_mentor(course_service: CourseService = Depends(get_course_service),
                             current_mentor: User = Depends(get_current_mentor)):

    courses = course_service.get_mentor_courses()

    return APIResponse(
        success=True,
        message="Courses retrieved successfully",
        data=CourseListResponse(
            courses=[
                CourseResponse(
                    course_name=course.name,
                    total_sections=course.total_section,
                    course_code=course.course_code
                )
                for course in courses
            ]
        )
    )
