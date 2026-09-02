from sqlalchemy.orm import Session

from app.models.course import Course


class CourseRepository:
    def __init__(self,db:Session):
        self.db=db

    def add_course(self,course):
        course_model=Course(**course.model_dump())
        self.db.add(course_model)
        self.db.commit()
        self.db.refresh(course_model)
        return course_model

    def find_course_by_course_code(self,course_code):
        return self.db.query(Course).filter(Course.course_code==course_code).first()