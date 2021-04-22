from sqlalchemy.orm import Session

from discord.dao.user_dao import UserDao
from discord.schema import User


class UserDaoImpl(UserDao):
    entity = User

    def __init__(self, engine: Session):
        self.engine = engine

    def get(self, uid: int):
        return self.engine.get(self.entity, uid)

    def get_all(self):
        return self.engine.query(self.entity).all()

    def post(self, user: User):
        self.engine.add(user)
        self.engine.commit()

    def put(self, user: User, uid: int):
        obj: User = self.engine.get(self.entity, uid)
        obj.nickname = user.nickname
        obj.image_url = user.image_url
        self.engine.add(obj)
        self.engine.commit()

