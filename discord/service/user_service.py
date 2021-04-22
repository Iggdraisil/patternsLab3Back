from discord.schema import User
from discord.service import GeneralService


class UserService(GeneralService):
    def get(self, id: int) -> User:
        return self.dao.get(id)

    def post(self, foo: User) -> None:
        pass

    def put(self, id: int, foo: User) -> None:
        pass

    def get_all(self) -> list[User]:
        pass
