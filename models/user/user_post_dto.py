from typing import Optional

from pydantic import BaseModel


class UserPostDto(BaseModel):
    login: str
    password: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: str
