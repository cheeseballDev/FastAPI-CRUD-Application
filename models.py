from beanie import Document
from pydantic import Field
from datetime import datetime
import uuid

"""This is a document model for MongoDB
Or so what I gathered from reading + watching... kinda like the skeleton? frame? of the database (well hence the name model fr)
Config is like how it should look like or serves as a template or example ig
Settings is how the database is set (like the name or idk havent searched too deep) 
Also trying to build a habit of adding comments to classes to explain them  
"""

class User(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    email: str
    created_at: datetime

    class Settings:
        name = "user_data"

    class Config:
        schema_extra={
            "id":"e7b7b2f6-8e02-4c9f-a6e0-03d5fa28d3b9",
            "name": "Matt",
            "email": "matt@example.com",
            "created_at": datetime.now(),
        }
