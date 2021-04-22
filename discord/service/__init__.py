from abc import ABC, abstractmethod

from discord.dao import GeneralDao
from discord.dao.csv_dao import CSVDao


class GeneralService(ABC):
    def __init__(self, dao: GeneralDao):
        self.dao = dao

    @abstractmethod
    def get(self, id: int) -> object:
        pass

    @abstractmethod
    def delete(self, id: int) -> object:
        pass

    @abstractmethod
    def post(self, foo: object) -> None:
        pass

    @abstractmethod
    def put(self, id: int, foo: object) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[object]:
        pass


class DBCreator(ABC):
    def __init__(self, csv_dao: CSVDao):
        self.csv_dao: CSVDao = csv_dao

    @abstractmethod
    def load_csv_and_create_db(self):
        pass
