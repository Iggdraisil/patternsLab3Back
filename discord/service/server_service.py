from discord.schema import Server
from discord.service import GeneralService


class ServerService(GeneralService):
    def get(self, id: int) -> Server:
        return self.dao.get(id)

    def post(self, foo: Server) -> None:
        pass

    def put(self, id: int, foo: Server) -> None:
        pass

    def get_all(self) -> list[Server]:
        pass
