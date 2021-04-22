from typing import Optional

from sqlalchemy.orm import Session

from discord.dao.message_dao import MessageDao
from discord.models import Message


class MessageDaoImpl(MessageDao):
    entity = Message

    def __init__(self, engine: Session):
        self.engine = engine

    def get(self, uid: int) -> Optional[Message]:
        return self.engine.get(self.entity, uid)

    def get_all(self):
        return self.engine.query(self.entity).all()

    def post(self, message: Message) -> Message:
        self.engine.add(message)
        self.engine.commit()
        return message

    def put(self, message: Message, uid: int) -> Message:
        obj: Message = self.engine.get(self.entity, uid)
        obj.text = message.text
        self.engine.add(obj)
        self.engine.commit()
        return obj

    def delete(self, id: int) -> Optional[Message]:
        obj = self.engine.get(self.entity, id)
        if not obj:
            return
        self.engine.delete(obj)
        self.engine.commit()
        return obj
