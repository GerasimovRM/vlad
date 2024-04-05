from fastapi import FastAPI

from server.controllers.user_controller import user_router

app = FastAPI(docs_url="/")
app.include_router(user_router)
