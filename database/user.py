from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base_meta import BaseSQLAlchemyModel


class User(BaseSQLAlchemyModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    messages = relationship("Message", back_populates="user")
    user_chats = relationship("UserChat", back_populates="user")