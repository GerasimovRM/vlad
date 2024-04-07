from fastapi import APIRouter

from database import get_session, Chat
from models.chat.chat_get_dto import ChatGetDto
from models.chat.chat_post_dto import ChatPostDto
from models.chat.chat_put_dto import ChatPutDto

chat_router = APIRouter(
    prefix="/chat",
    tags=["chat"])


@chat_router.post("/", response_model=ChatGetDto)
def create_chat(chat_dto: ChatPostDto):
    session = get_session()
    # new_chat = Chat(login=chat_dto.login,
    #                 password=chat_dto.password,
    #                 first_name=chat_dto.first_name,
    #                 middle_name=chat_dto.middle_name,
    #                 last_name=chat_dto.last_name,
    #                 email=chat_dto.email)
    new_chat = Chat(**chat_dto.model_dump())
    session.add(new_chat)
    session.commit()
    response = ChatGetDto(**new_chat.to_dict())
    session.close()
    return response


@chat_router.get("/", response_model=ChatGetDto)
def get_chat(id: int):
    session = get_session()
    chat = session.query(Chat).get(id)
    response = ChatGetDto(**chat.to_dict())
    session.close()
    return response


@chat_router.put("/", response_model=ChatGetDto)
def put_chat(id: int, chat_dto: ChatPutDto):
    session = get_session()
    chat = session.query(Chat).get(id)
    chat.update_by_pydantic(chat_dto)
    session.commit()
    response = ChatGetDto(**chat.to_dict())
    session.close()
    return response


@chat_router.delete("/")
def delete_chat(id: int):
    session = get_session()
    chat = session.query(Chat).get(id)
    session.delete(chat)
    session.commit()
    session.close()
