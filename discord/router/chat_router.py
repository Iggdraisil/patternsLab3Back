from fastapi import APIRouter, Depends

router = APIRouter(prefix='/chat')


@router.get('/{chat_id}')
def get_chat(chat_id: int, chat_service=Depends()):
    pass


@router.post('/')
def post_chat(chat_service=Depends()):
    pass


@router.put('/{chat_id}')
def put_chat(chat_service=Depends()):
    pass