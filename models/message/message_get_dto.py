from datetime import datetime

from models.message.message_post_dto import MessagePostDto


class MessageGetDto(MessagePostDto):
    id: int
    time: datetime
