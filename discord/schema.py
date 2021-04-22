from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel

from discord.models import Message


class ORMBase(BaseModel):
    class Config:
        orm_mode = True


class User(ORMBase):
    id: int
    nickname: str
    image_url: str

    @classmethod
    def from_orm(cls, obj):
        return super().from_orm(obj)


class BaseMessageSchema(ORMBase):
    text: str


class SendMessageSchema(BaseMessageSchema):
    sender_id: int
    chat_id: int


class Server(ORMBase):
    id: int
    name: str
    image_url: str


class Chat(ORMBase):
    id: int
    name: str
    server: Server

    @classmethod
    def from_orm(cls, obj):
        value = super().from_orm(obj)
        value.server = Server.from_orm(obj.server)
        return value


class MessageSchema(BaseMessageSchema):
    id: int
    time: datetime
    sender: User
    chat: Chat

    @classmethod
    def from_orm(cls, obj: Message):
        value = super().from_orm(obj)
        value.sender = obj.sender
        value.chat = obj.chat
        return value
