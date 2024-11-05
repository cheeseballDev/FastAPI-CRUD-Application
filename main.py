from fastapi import FastAPI
from users import user_router
from database import start_database

app = FastAPI()

async def connect():
    await start_database()

app.include_router(user_router)