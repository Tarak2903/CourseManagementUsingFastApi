from sqlalchemy.exc import IntegrityError

from app.exceptions.ResrouceAlreadyExistsException import ResourceAlreadyExistsException
from app.models.course import Course
from app.repositories.CourseRepository import CourseRepository


class CourseService:
    def __init__(self,course_repo:CourseRepository):
        self.course_repo=course_repo

    def add_course(self,course):
        try:
            self.course_repo.add_course(course)
        except IntegrityError:
            raise ResourceAlreadyExistsException("Course with this id already exists")

    def get_mentor_courses(self):
        return self.course_repo.get_mentor_courses()
