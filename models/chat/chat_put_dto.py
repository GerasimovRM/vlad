from typing import Optional

from pydantic import BaseModel


class ChatPutDto(BaseModel):
    name: Optional[str] = None
