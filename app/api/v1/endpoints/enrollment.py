from fastapi import APIRouter, Depends

from app.core.dependency import get_enrollment_service
from app.core.security import get_current_mentor, get_current_intern
from app.models.user import User
from app.schemas.Course.CourseSectionCompletionStatus import CourseSectionCompletionStatus
from app.schemas.Enrollment.EnrollmentRequest import EnrollmentRequest
from app.services.EnrollmentService import EnrollmentService

router=APIRouter()


@router.post('/enrollments',tags=['Mentor'])
async def enroll_intern(enrollment_request:EnrollmentRequest,
                  enrollment_service:EnrollmentService=Depends(get_enrollment_service),
                  mentor:User=Depends(get_current_mentor)):
    return enrollment_service.enroll_intern(enrollment_request,mentor.id)

@router.get('/enrollments/{intern_id}',tags=['Mentor'])
async def get_intern_progress(intern_id,
                        enrollment_service:EnrollmentService=Depends(get_enrollment_service),
                        mentor:User=Depends(get_current_mentor)):
    return enrollment_service.get_intern_progress(intern_id)

@router.get('/enrollments/courses',tags=['Intern'])
def get_interns_course(enrollment_service:EnrollmentService=Depends(get_enrollment_service),intern:User=Depends(get_current_intern)):
    return enrollment_service.get_interns_courses(intern.id)

@router.get('/enrollment/courses/{course_id}',tags=['Intern'])
def get_interns_course_info(course_id,enrollment_service:EnrollmentService=Depends(get_enrollment_service),
                            intern:User=Depends(get_current_intern)):
    return enrollment_service.get_intern_course_info(course_id,intern.id)

@router.put("/enrollment/courses/{course_id}",tags=['Intern'])
def complete_course_section(course_id,course:CourseSectionCompletionStatus,
                            enrollment_service:EnrollmentService=Depends(get_enrollment_service),intern:User=Depends(get_current_intern)):
    return enrollment_service.complete_section(course_id,course,intern.id)

