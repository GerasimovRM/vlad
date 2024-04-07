from typing import List

from fastapi import APIRouter

from database import get_session, Message, Chat
from models.message.message_beautiful_for_chat_dto import MessageBeautifulForChatDto
from models.message.message_get_dto import MessageGetDto
from models.message.message_post_dto import MessagePostDto
from models.message.message_put_dto import MessagePutDto
from models.user.user_get_dto import UserGetDto

message_router = APIRouter(
    prefix="/message",
    tags=["message"])


@message_router.post("/", response_model=MessageGetDto)
def create_message(message_dto: MessagePostDto):
    session = get_session()
    # new_message = Message(login=message_dto.login,
    #                 password=message_dto.password,
    #                 first_name=message_dto.first_name,
    #                 middle_name=message_dto.middle_name,
    #                 last_name=message_dto.last_name,
    #                 email=message_dto.email)
    new_message = Message(**message_dto.model_dump())
    session.add(new_message)
    session.commit()
    response = MessageGetDto(**new_message.to_dict())
    session.close()
    return response


@message_router.get("/", response_model=MessageGetDto)
def get_message(id: int):
    session = get_session()
    message = session.query(Message).get(id)
    response = MessageGetDto(**message.to_dict())
    session.close()
    return response


@message_router.put("/", response_model=MessageGetDto)
def put_message(id: int, message_dto: MessagePutDto):
    session = get_session()
    message = session.query(Message).get(id)
    message.update_by_pydantic(message_dto)
    session.commit()
    response = MessageGetDto(**message.to_dict())
    session.close()
    return response


@message_router.delete("/")
def delete_message(id: int):
    session = get_session()
    message = session.query(Message).get(id)
    session.delete(message)
    session.commit()
    session.close()


@message_router.get("/get-all-from-chat", response_model=List[MessageBeautifulForChatDto])
def get_all_from_chat(chat_id: int):
    session = get_session()
    chat: Chat = session.query(Chat).get(chat_id)
    messages = []
    for message in sorted(chat.messages, key=lambda m: m.time):
        response = MessageBeautifulForChatDto(message_id=message.id,
                                              text=message.text,
                                              user=UserGetDto(**message.user.to_dict()),
                                              time=message.time)
        messages.append(response)
    return messages
