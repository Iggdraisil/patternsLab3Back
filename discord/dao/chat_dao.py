from abc import abstractmethod

from discord.dao import GeneralDao
from discord.models import Chat


class ChatDao(GeneralDao):
    @abstractmethod
    def get(self, uid: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def post(self, chat: Chat):
        pass

    @abstractmethod
    def put(self, chat: Chat, uid: int):
        pass
