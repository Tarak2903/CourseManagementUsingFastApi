from app.exceptions.user_exceptions import UserAlreadyExistsException

class UserService:
    def __init__(self,user_repo):
        self.user_repo=user_repo

    def add_user(self,user):
        if self.user_repo.check_user_name_exists(user.user_name):
            raise UserAlreadyExistsException("User already exists")

        self.user_repo.add_user(user)
