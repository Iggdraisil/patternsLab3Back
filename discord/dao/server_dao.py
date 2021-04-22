from abc import abstractmethod

from discord.dao import GeneralDao
from discord.models import Server


class ServerDao(GeneralDao):
    @abstractmethod
    def get(self, uid: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def post(self, server: Server):
        pass

    @abstractmethod
    def put(self, server: Server, uid: int):
        pass
