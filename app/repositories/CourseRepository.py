from sqlalchemy.orm import Session


class CourseRepository:
    def __init__(self,db:Session):
        self.db=db

