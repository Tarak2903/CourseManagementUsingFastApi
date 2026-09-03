from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.Auth.SignupRequest import SignupRequest


class AuthRepository:
    def __init__(self,db:Session):
        self.db=db


    def find_user_by_username(self,user_name):
        return (
            self.db.query(User).filter(User.user_name==user_name).first()
        )

    # def add_user(self,user:SignupRequest):
    #     user_model=User(**user.model_dump())
    #     self.db.add(user_model)
    #     self.db.commit()
