from sqlalchemy.exc import SQLAlchemyError

from app.user.models import User


class ShopDB:
    def __init__(self, session):
        self.__session = session

    def add_user(self, username: str, password: str) -> bool:
        try:
            if User.query.filter_by(username=username).first():
                print("Пользователь с таким псевдонимом уже существует")
                return False
            user = User(username=username, password=password)
            self.__session.add(user)
            self.__session.commit()
        except SQLAlchemyError as err:
            print('Ошибка при добавление нового пользователя ' + str(err))
            return False
        return True

    @staticmethod
    def get_user(user_id: int):
        try:
            user = User.query.filter_by(id=user_id).first()
            if not user:
                print('Пользователь не найден')
                return False
            return user
        except SQLAlchemyError as err:
            print('Ошибка при получение данных из БД ' + str(err))
        return False

    @staticmethod
    def get_user_by_username(username):
        try:
            user = User.query.filter_by(username=username).first()
            if not user:
                print('Пользователь не найден')
                return False
            return user
        except SQLAlchemyError as err:
            print('Ошибка при получение данных из БД ' + str(err))
        return False
