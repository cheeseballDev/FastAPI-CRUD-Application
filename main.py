from fastapi import FastAPI
from users import user_router
from database import init_database
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_database()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_router)