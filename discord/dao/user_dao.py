from abc import abstractmethod

from discord.dao import GeneralDao
from discord.models import User


class UserDao(GeneralDao):
    @abstractmethod
    def get(self, uid: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def post(self, user: User):
        pass

    @abstractmethod
    def put(self, user: User, uid: int):
        pass
