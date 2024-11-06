import os
import beanie
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from models import User

load_dotenv()

async def init_database():
    client = AsyncIOMotorClient(os.getenv('MONGODB_URL'))
    await beanie.init_beanie(database = client.db_name, document_models = [User])