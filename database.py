import beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import User
async def connect_database():
    client = AsyncIOMotorClient("mongodb://localhost:3000")
    await beanie.init_beanie(
        database = client.db_name,
        document_models = [User]
    )