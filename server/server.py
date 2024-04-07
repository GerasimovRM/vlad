from fastapi import FastAPI

from server.controllers.chat_controller import chat_router
from server.controllers.message_controller import message_router
from server.controllers.user_controller import user_router

app = FastAPI(docs_url="/")
app.include_router(user_router)
app.include_router(chat_router)
app.include_router(message_router)
