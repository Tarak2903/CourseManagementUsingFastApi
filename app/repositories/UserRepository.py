from app.models.user import User


class UserRepository:

    def __init__(self, db):
        self.db = db

    def check_user_name_exists(self, user_name):
        return (
            self.db.query(User)
            .filter(User.user_name == user_name)
            .first()
            is not None
        )

    def add_user(self, user):
        user_model = User(**user.model_dump())

        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)

        return user_model