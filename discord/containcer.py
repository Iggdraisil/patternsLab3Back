from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import DependenciesContainer, Singleton, Container, Resource

from discord.dao.chat_dao import ChatDao
from discord.dao.chat_dao_imp import ChatDaoImpl
from discord.dao.csv_dao import CSVDao
from discord.dao.csv_dao_impl import CSVDaoImpl
from discord.dao.message_dao import MessageDao
from discord.dao.message_dao_imp import MessageDaoImpl
from discord.dao.server_dao import ServerDao
from discord.dao.server_dao_imp import ServerDaoImpl
from discord.dao.user_dao import UserDao
from discord.dao.user_dao_imp import UserDaoImpl
from discord.db import get_db
from discord.service import DBCreator
from discord.service.chat_service import ChatService
from discord.service.db_creator import DBCreatorImpl
from discord.service.message_service import MessageService
from discord.service.server_service import ServerService
from discord.service.user_service import UserService


class DAO(DeclarativeContainer):
    engine = Resource(get_db)
    chat_dao: ChatDao = Singleton(ChatDaoImpl, engine)
    message_dao: MessageDao = Singleton(MessageDaoImpl, engine)
    server_dao: ServerDao = Singleton(ServerDaoImpl, engine)
    user_dao: UserDao = Singleton(UserDaoImpl, engine)
    csv_dao: CSVDao = Singleton(CSVDaoImpl, 'data.scv')


class Service(DeclarativeContainer):
    dao = DependenciesContainer()
    chat_srv = Singleton(ChatService, dao=dao.chat_dao)
    message_srv = Singleton(MessageService, dao=dao.message_dao)
    server_srv = Singleton(ServerService, dao=dao.server_dao)
    user_srv = Singleton(UserService, dao=dao.user_dao)
    db_creator: DBCreator = Singleton(
        DBCreatorImpl,
        dao.csv_dao,
        dao.chat_dao,
        dao.message_dao,
        dao.user_dao,
        dao.server_dao
    )


class Core(DeclarativeContainer):
    dao = Container(DAO)
    service = Container(Service, dao=dao)
