from typing import Optional

from pydantic import BaseModel


class ChatPostDto(BaseModel):
    name: str
