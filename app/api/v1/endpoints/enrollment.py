from fastapi import APIRouter, Depends

from app.core.dependency import get_enrollment_service
from app.core.security import get_current_mentor
from app.models.user import User
from app.schemas.Enrollment.EnrollmentRequest import EnrollmentRequest
from app.services.EnrollmentService import EnrollmentService

router=APIRouter()


@router.post('/enrollments',tags=['Mentor'])
def enroll_intern(enrollment_request:EnrollmentRequest,
                  enrollment_service:EnrollmentService=Depends(get_enrollment_service),
                  mentor:User=Depends(get_current_mentor)):
    return enrollment_service.enroll_intern(enrollment_request,mentor.id)