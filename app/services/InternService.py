from pwdlib import PasswordHash

from app.exceptions.user_exceptions import UserAlreadyExistsException
from app.repositories.InternRepository import InternRepository
from app.schemas.Intern.InternCreationRequest import InternCreationRequest
from app.schemas.Intern.InternResponse import InternResponse


class InternService:
    def __init__(self,intern_repo:InternRepository):
        self.intern_repo=intern_repo
        self.password_hash=PasswordHash.recommended()

    def get_course(self,user):
        return self.intern_repo.get_course(user)

    def get_course_by_id(self,intern_id,user):
        return self.intern_repo.get_course_by_id(intern_id,user)

    def add_intern(self,intern:InternCreationRequest,mentor_id):
        intern.password=self.password_hash.hash(intern.password)
        if self.intern_repo.find_intern_by_username(intern.user_name) is not None:
            raise UserAlreadyExistsException("User already exists")
        return self.intern_repo.add_intern(intern,mentor_id)

    def get_interns_by_mentor_id(self,mentor_id):
        ls= self.intern_repo.get_interns_by_mentor_id(mentor_id)
        interns=[]
        [interns.append(InternResponse(intern_name=intern.name,intern_user_name=intern.user_name)) for intern in ls]
        return interns

