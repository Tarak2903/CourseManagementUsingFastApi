from app.repositories.UserRepository import UserRepository


class UserService:
    def __init__(self,user_repo:UserRepository):
        self.user_repo=user_repo




