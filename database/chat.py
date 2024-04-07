from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base_meta import BaseSQLAlchemyModel


class Chat(BaseSQLAlchemyModel):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    messages = relationship("Message", back_populates="chat")
    chat_users = relationship("UserChat", back_populates="chat")
