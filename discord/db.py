import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///discord.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
meta = MetaData(bind=engine)
Base: sqlalchemy.schema.Table = declarative_base(metadata=meta)


def get_db() -> Session:
    engine.connect()
    Base.metadata.create_all(checkfirst=True)
    db: Session = SessionLocal()
    return db
