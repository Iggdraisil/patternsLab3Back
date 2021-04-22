from abc import abstractmethod

from discord.dao import GeneralDao
from discord.models import Message


class MessageDao(GeneralDao):
    @abstractmethod
    def get(self, uid: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def post(self, chat: Message):
        pass

    @abstractmethod
    def put(self, chat: Message, uid: int):
        pass
