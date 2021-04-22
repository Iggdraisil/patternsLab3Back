from sqlalchemy.orm import Session

from discord.dao.server_dao import ServerDao
from discord.models import Server


class ServerDaoImpl(ServerDao):
    entity = Server

    def __init__(self, engine: Session):
        self.engine = engine

    def get(self, uid: int):
        return self.engine.get(self.entity, uid)

    def get_all(self):
        return self.engine.query(self.entity).all()

    def post(self, message: Server):
        self.engine.add(message)
        self.engine.commit()

    def put(self, server: Server, uid: int):
        obj: Server = self.engine.get(self.entity, uid)
        obj.name = server.name
        obj.image_url = server.image_url
        self.engine.add(obj)
        self.engine.commit()
