from sqlalchemy.orm import Session


class MentorRepository:
    def __init__(self,db:Session):
        self.db=db


    