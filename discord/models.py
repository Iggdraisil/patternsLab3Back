from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Time, DateTime
from sqlalchemy.orm import relationship

from discord.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String)
    image_url = Column(String)
    messages = relationship("Message", back_populates="sender")


class Server(Base):
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True, index=True)
    chats = relationship("Chat",  back_populates="server")
    name = Column(String)
    image_url = Column(String)


class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    server_id = Column(Integer, ForeignKey('servers.id'))
    server = relationship("Server",  back_populates="chats")
    messages = relationship("Message", back_populates="chat")


class Message(Base):
    def __init__(self, time=None, read=False, *args, **kwargs):
        if isinstance(time, str):
            self.time = datetime.fromisoformat(time)
        elif isinstance(time, datetime):
            self.time = time
        if isinstance(read, str):
            self.read = eval(read)
        else:
            self.read = read
        super().__init__(*args, **kwargs)

    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(String, ForeignKey('users.id'))
    chat_id = Column(String, ForeignKey('chats.id'))
    chat = relationship("Chat", back_populates="messages")
    sender = relationship("User", back_populates="messages")
    time = Column(DateTime, default=datetime.now())
    text = Column(String)
    read = Column(Boolean)
