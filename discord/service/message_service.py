import datetime
from typing import Optional

from discord.models import Message
from discord.schema import MessageSchema, SendMessageSchema, BaseMessageSchema
from discord.service import GeneralService


class MessageService(GeneralService):
    def delete(self, id: int) -> Optional[MessageSchema]:
        msg = self.dao.delete(id)
        return MessageSchema.from_orm(msg) if msg else None

    def get(self, id: int) -> Optional[MessageSchema]:
        msg = self.dao.get(id)
        return MessageSchema.from_orm(msg) if msg else None

    def post(self, foo: SendMessageSchema) -> None:
        return MessageSchema.from_orm(self.dao.post(Message(**foo.dict(), read=False)))

    def put(self, id: int, foo: BaseMessageSchema) -> None:
        return MessageSchema.from_orm(self.dao.put(Message(**foo.dict()), id))

    def get_all(self) -> list[MessageSchema]:
        return [MessageSchema.from_orm(msg) for msg in self.dao.get_all()]
