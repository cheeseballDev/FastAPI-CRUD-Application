import beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models import User

async def init_database():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await beanie.init_beanie(database = client.db_name, document_models = [User])