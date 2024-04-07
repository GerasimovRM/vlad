from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.base_meta import Base, BaseSQLAlchemyModel


class Message(BaseSQLAlchemyModel):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey("chat.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    text = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")