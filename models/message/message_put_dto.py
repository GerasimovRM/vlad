from pydantic import BaseModel


class MessagePutDto(BaseModel):
    text: str
