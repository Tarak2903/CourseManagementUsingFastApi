from app.exceptions.ForbiddenException import ForbiddenException
from app.exceptions.InvalidOperationException import InvalidOperationException
from app.exceptions.course_exceptions import CourseNotFoundException
from app.models.course import Course
from app.models.enrollment import Enrollment
from app.repositories.CourseRepository import CourseRepository
from app.repositories.InternRepository import InternRepository
from app.schemas.Course.InternCourseResponse import InternCourseResponse
from app.schemas.Course.InternCourseProgressResponse import InternProgressResponse
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

    def get_intern_progress(self,intern_id):
        intern_progress=self.enrollment_repo.get_intern_progress(intern_id)
        intern_progress_response=[]
        for enrollment,course in intern_progress:
            intern_progress_model=InternProgressResponse(course_name=course.name,total_sections=course.total_section,
            sections_completed=enrollment.section_completed,percentage_completed=enrollment.section_completed/course.total_section)
            intern_progress_response.append(intern_progress_model)

        return intern_progress_response

    def get_interns_courses(self,intern_id):
        courses_model=self.enrollment_repo.get_interns_courses(intern_id)
        courses=[]
        [courses.append(InternCourseResponse(course_name=course.name,total_sections=course.total_section))
         for enrollment,course in courses_model]
        return courses

    def get_intern_course_info(self,course_id,intern_id):
        enrollment,course= self.enrollment_repo.get_intern_course_info(course_id,intern_id)
        return InternProgressResponse(course_name=course.name,total_sections=course.total_section,
                                      sections_completed=enrollment.section_completed,
                                      percentage_completed=enrollment.section_completed/course.total_section*100)

    def complete_section(self,course_id,course,intern_id):
        section_completed,total_sections=self.enrollment_repo.section_request_validation(course_id,intern_id)
        if section_completed+course.section>total_sections:
            raise InvalidOperationException("Sections exceeded than the total sections")
        self.enrollment_repo.complete_section(course_id,intern_id,course.section)