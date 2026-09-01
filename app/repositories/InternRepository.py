from sqlalchemy.orm import Session

from app.models.enrollment import Enrollment


class InternRepository:
    def __init__(self,db:Session):
        self.db=db

    def get_course(self,user):
        return self.db.query(Enrollment).filter(Enrollment.intern_id==user.id).all()

    def get_course_by_id(self,intern_id,user):
        pass