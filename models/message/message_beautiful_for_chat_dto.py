from datetime import datetime

from pydantic import BaseModel

from models.user.user_get_dto import UserGetDto


class MessageBeautifulForChatDto(BaseModel):
    message_id: int
    user: UserGetDto
    text: str
    time: datetime
