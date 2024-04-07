from typing import Optional

from pydantic import BaseModel


class MessagePostDto(BaseModel):
    chat_id: int
    user_id: int
    text: str

