from sqlalchemy.orm import Session

from app.core.enums import Role
from app.models.enrollment import Enrollment
from app.models.user import User


class InternRepository:
    def __init__(self,db:Session):
        self.db=db

    def get_course(self,user):
        return self.db.query(Enrollment).filter(Enrollment.intern_id==user.id).all()

    def get_course_by_id(self,intern_id,user):
        pass

    def add_intern(self,intern,user_mentor_id):
        intern_model=User(**intern.model_dump(),role=Role.INTERN,mentor_id=user_mentor_id)
        self.db.add(intern_model)
        self.db.commit()
        self.db.refresh(intern_model)
        return intern_model

    def find_intern_by_username(self,user_name):
        return self.db.query(User).filter(User.user_name==user_name).first()

    def find_interns_by_mentor_id(self,mentor_id):
        results = self.db.query(User.id).filter(User.mentor_id == mentor_id).all()
        return [row.id for row in results]

    def get_interns_by_mentor_id(self,mentor_id):
        return self.db.query(User).filter(User.mentor_id==mentor_id).all()
