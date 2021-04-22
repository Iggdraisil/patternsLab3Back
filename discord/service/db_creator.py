from discord.dao.chat_dao import ChatDao
from discord.dao.csv_dao import CSVDao
from discord.dao.message_dao import MessageDao
from discord.dao.server_dao import ServerDao
from discord.dao.user_dao import UserDao
from discord.models import User, Chat, Message, Server
from discord.service import DBCreator


class DBCreatorImpl(DBCreator):
    def __init__(
            self,
            csv_dao: CSVDao,
            chat_dao: ChatDao,
            message_dao: MessageDao,
            user_dao: UserDao,
            server_dao: ServerDao
    ):
        super().__init__(csv_dao)
        self.mapping = {
            'user': (
                user_dao, User
            ),
            'chat': (
                chat_dao, Chat
            ),
            'message': (
                message_dao, Message
            ),
            'server': (
                server_dao, Server
            ),
        }

    def load_csv_and_create_db(self):
        data = self.csv_dao.read_from_file()
        keys = []
        data_type = None
        loaded = {}
        for line in data:
            if len(line) == 0:
                keys = None
                continue
            if not keys:
                keys = line[:-1]
                data_type = line[-1]
                loaded[data_type] = []
                continue
            self.mapping[data_type][0].post(self.mapping[data_type][1](**dict(zip(keys, line))))
