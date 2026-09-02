from app.exceptions.ForbiddenException import ForbiddenException
from app.exceptions.course_exceptions import CourseNotFoundException
from app.repositories.CourseRepository import CourseRepository
from app.repositories.InternRepository import InternRepository
from app.schemas.Enrollment.EnrollmentRequest import EnrollmentRequest


class EnrollmentService:
    def __init__(self,enrollment_repo,intern_repo:InternRepository,course_repo:CourseRepository):
        self.enrollment_repo=enrollment_repo
        self.intern_repo=intern_repo
        self.course_repo=course_repo

    def enroll_intern(self,enrollment_request:EnrollmentRequest,mentor_id:int):
        ls_interns=enrollment_request.interns
        course_code=enrollment_request.course_code
        interns=self.intern_repo.find_interns_by_mentor_id(mentor_id)
        for intern_id in ls_interns:
            if intern_id not in interns:
                raise ForbiddenException("You do not have access to manage one of the intern(s)")

        course=self.course_repo.find_course_by_course_code(course_code)

        if course is None:
            raise CourseNotFoundException("Course with this code deos not  exist")


        return self.enrollment_repo.enroll_intern(ls_interns,course.id)

