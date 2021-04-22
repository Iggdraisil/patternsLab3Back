from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from discord.containcer import Core
from discord.schema import MessageSchema, SendMessageSchema, BaseMessageSchema
from discord.service.message_service import MessageService

message_router = APIRouter(prefix='/messages')


@message_router.get('/{message_id}', response_model=MessageSchema)
@inject
async def get_message(message_id: int, msg_service: MessageService = Depends(Provide[Core.service.message_srv])):
    obj = msg_service.get(message_id)
    if not obj:
        raise HTTPException(status_code=404, detail='This message not found')
    return obj


@message_router.get('/', response_model=list[MessageSchema])
@inject
async def get_messages(msg_service: MessageService = Depends(Provide[Core.service.message_srv])):
    return msg_service.get_all()


@message_router.post('/', response_model=MessageSchema)
@inject
async def post_message(
        message: SendMessageSchema,
        msg_service: MessageService = Depends(Provide[Core.service.message_srv])
):
    return msg_service.post(message)


@message_router.put('/{message_id}', response_model=MessageSchema)
@inject
async def put_message(
        message_id: int,
        message: BaseMessageSchema,
        msg_service: MessageService = Depends(Provide[Core.service.message_srv])
):
    return msg_service.put(message_id, message)


@message_router.delete('/{message_id}', response_model=MessageSchema)
@inject
async def put_message(
        message_id: int,
        msg_service: MessageService = Depends(Provide[Core.service.message_srv])
):
    obj = msg_service.delete(message_id)
    if not obj:
        raise HTTPException(status_code=404, detail='This message not found')
    return obj
