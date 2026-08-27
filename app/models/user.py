from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    user_name=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    role=Column(String,nullable=False)
    mentor_id=Column(Integer,ForeignKey("users.id"),nullable=True)
