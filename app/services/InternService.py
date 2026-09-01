from app.repositories.InternRepository import InternRepository


class InternService:
    def __init__(self,intern_repo:InternRepository):
        self.intern_repo=intern_repo

    def get_course(self,user):
        return self.intern_repo.get_course(user)

    def get_course_by_id(self,intern_id,user):
        return self.intern_repo.get_course_by_id(intern_id,user)
