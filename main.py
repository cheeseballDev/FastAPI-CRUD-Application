from contextlib import asynccontextmanager
from fastapi import FastAPI
from users import user_router
from database import connect_database

app = FastAPI(lifespan=lifespan)

@asynccontextmanager
async def lifespan():
    await connect_database()

app.include_router(user_router)