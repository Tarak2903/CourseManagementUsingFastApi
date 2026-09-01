from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.CourseRepository import CourseRepository
from app.repositories.MentorRepository import MentorRepository
from app.repositories.AuthRepository import AuthRepository
from app.repositories.InternRepository import InternRepository
from app.core.database import get_db
from app.services.CourseService import CourseService
from app.services.MentorService import MentorService
from app.services.AuthService import AuthService
from app.services.InternService import InternService

def get_intern_repository(db:Session=Depends(get_db)):
    return InternRepository(db)

def get_intern_service(user_repo:InternRepository=Depends(get_intern_repository)):
    return InternService(user_repo)


def get_auth_repository(db:Session=Depends(get_db)):
    return AuthRepository(db)

def get_auth_service(auth_repo:AuthRepository=Depends(get_auth_repository)):
    return AuthService(auth_repo)

def get_mentor_repository(db:Session=Depends(get_db)):
    return MentorRepository(db)

def get_mentor_service(mentor_repo:MentorRepository=Depends(get_mentor_repository)):
    return MentorService(mentor_repo)

def get_course_repository(db:Session=Depends(get_db)):
    return CourseRepository(db)

def get_course_service(course_repo:CourseRepository=Depends(get_course_repository)):
    return CourseService(course_repo)