from abc import abstractmethod, ABC


class GeneralDao(ABC):
    def __init__(self, engine):
        self.engine = engine

    @abstractmethod
    def get(self, uid: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def post(self, foo: object):
        pass

    @abstractmethod
    def put(self, foo: object, uid: int):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
