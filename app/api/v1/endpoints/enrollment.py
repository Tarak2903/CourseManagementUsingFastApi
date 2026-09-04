from fastapi import APIRouter, Depends

from app.core.dependency import get_enrollment_service
from app.core.security import get_current_mentor, get_current_intern
from app.models.user import User
from app.schemas.APIResponse import APIResponse
from app.schemas.Course.CourseSectionCompletionStatus import CourseSectionCompletionStatus
from app.schemas.Course.InternCourseResponse import InternCourseResponse
from app.schemas.Course.InternCourseProgressResponse import InternProgressResponse
from app.schemas.Course.InternProgressListResponse import InternProgressListResponse
from app.schemas.Course.SectionCompletionResponse import SectionCompletionResponse
from app.schemas.Enrollment.EnrollmentRequest import EnrollmentRequest
from app.schemas.Enrollment.EnrollmentResponse import EnrollmentResponse
from app.services.EnrollmentService import EnrollmentService

router = APIRouter()


@router.post('/enrollments', response_model=APIResponse[EnrollmentResponse], tags=['Mentor'])
async def enroll_intern(enrollment_request: EnrollmentRequest,
                        enrollment_service: EnrollmentService = Depends(get_enrollment_service),
                        mentor: User = Depends(get_current_mentor)):

    enrollment_service.enroll_intern(enrollment_request, mentor.id)

    return APIResponse(
        success=True,
        message="Intern(s) enrolled successfully",
        data=EnrollmentResponse(
            course_code=enrollment_request.course_code,
            interns=enrollment_request.interns
        )
    )


@router.get('/enrollments/{intern_id}', response_model=APIResponse[InternProgressListResponse], tags=['Mentor'])
async def get_intern_progress(intern_id,
                              enrollment_service: EnrollmentService = Depends(get_enrollment_service),
                              mentor: User = Depends(get_current_mentor)):

    progress = enrollment_service.get_intern_progress(intern_id)

    return APIResponse(
        success=True,
        message="Intern progress retrieved successfully",
        data=InternProgressListResponse(progress=progress)
    )


@router.get('/enrollments/courses', response_model=APIResponse[dict], tags=['Intern'])
def get_interns_course(enrollment_service: EnrollmentService = Depends(get_enrollment_service),
                       intern: User = Depends(get_current_intern)):

    courses = enrollment_service.get_interns_courses(intern.id)

    return APIResponse(
        success=True,
        message="Enrolled courses retrieved successfully",
        data={
            "courses": [course.model_dump() for course in courses]
        }
    )


@router.get('/enrollment/courses/{course_id}', response_model=APIResponse[InternProgressResponse], tags=['Intern'])
def get_interns_course_info(course_id,
                            enrollment_service: EnrollmentService = Depends(get_enrollment_service),
                            intern: User = Depends(get_current_intern)):

    course_info = enrollment_service.get_intern_course_info(course_id, intern.id)

    return APIResponse(
        success=True,
        message="Course progress retrieved successfully",
        data=course_info
    )


@router.put("/enrollment/courses/{course_id}", response_model=APIResponse[SectionCompletionResponse], tags=['Intern'])
def complete_course_section(course_id, course: CourseSectionCompletionStatus,
                            enrollment_service: EnrollmentService = Depends(get_enrollment_service),
                            intern: User = Depends(get_current_intern)):

    enrollment_service.complete_section(course_id, course, intern.id)

    return APIResponse(
        success=True,
        message="Course section completed successfully",
        data=SectionCompletionResponse(
            sections_completed_in_this_operation=course.section
        )
    )
