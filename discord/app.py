import sys

from dependency_injector.wiring import inject, Provide
from fastapi import FastAPI

from discord import router
from discord.containcer import Core
from discord.router.message_router import message_router
from discord.service import DBCreator


@inject
def main(db_creator: DBCreator = Provide[Core.service.db_creator]):
    db_creator.load_csv_and_create_db()


def get_app():
    core = Core()
    core.wire(packages=[router], modules=[sys.modules[__name__]])
    appf = FastAPI()
    appf.container = core
    appf.include_router(message_router)
    return appf


app = get_app()
