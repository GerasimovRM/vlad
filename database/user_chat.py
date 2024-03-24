from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base_meta import Base, BaseSQLAlchemyModel


class UserChat(BaseSQLAlchemyModel):
    __tablename__ = "user_chat"

    chat_id = Column(ForeignKey("chat.id"), primary_key=True)
    user_id = Column(ForeignKey("user.id"), primary_key=True)

    chat = relationship("Chat", back_populates="chat_users")
    user = relationship("User", back_populates="user_chats")

