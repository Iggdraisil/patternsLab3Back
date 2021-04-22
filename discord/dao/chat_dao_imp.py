from sqlalchemy.orm import Session

from discord.dao.chat_dao import ChatDao
from discord.models import Chat


class ChatDaoImpl(ChatDao):
    entity = Chat

    def __init__(self, engine: Session):
        self.engine = engine

    def get(self, uid: int):
        return self.engine.get(self.entity, uid)

    def get_all(self):
        return self.engine.query(self.entity).all()

    def post(self, chat: Chat):
        self.engine.add(chat)
        self.engine.commit()

    def put(self, chat: Chat, uid: int):
        obj: Chat = self.engine.get(self.entity, uid)
        obj.name = chat.name
        self.engine.add(obj)
        self.engine.commit()
        return obj

    def delete(self, id: int) -> None:
        obj = self.engine.get(self.entity, id)
        self.engine.delete(obj)
        self.engine.commit()
        return obj

