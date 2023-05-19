from flask_login import UserMixin


class UserLogin(UserMixin):
    def __init__(self):
        self.__user = None

    def from_db(self, user_id: int, db):
        self.__user = db.get_user(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user.id)

    def get_username(self):
        return str(self.__user.username)

    def get_fullname(self):
        return f"{self.__user.first_name} {self.__user.last_name}"
