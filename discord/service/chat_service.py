from discord.schema import Chat
from discord.service import GeneralService


class ChatService(GeneralService):
    def get(self, id: int) -> Chat:
        return self.dao.get(id)

    def post(self, foo: Chat) -> None:
        pass

    def put(self, id: int, foo: Chat) -> None:
        pass

    def get_all(self) -> list[Chat]:
        pass
