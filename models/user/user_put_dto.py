from typing import Optional

from pydantic import BaseModel


class UserPutDto(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
