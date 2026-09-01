from app.repositories.CourseRepository import CourseRepository


class CourseService:
    def __init__(self,course_repo:CourseRepository):
        self.course_repo=course_repo