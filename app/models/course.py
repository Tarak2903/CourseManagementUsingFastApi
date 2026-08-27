from sqlalchemy import Integer,Column,String

from app.core.database import Base

class Course(Base):
    __tablename__ = 'course'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    total_section=Column(String,nullable=False)