from beanie import Document
from pydantic import Field
from datetime import datetime
import uuid

class User(Document):
    """This is a document model for the user
    kinda like the skeleton? frame? of the database (well hence the name model fr)
    Config is like how it should look like or serves as a template or example ig
    Settings is how the database is set (like the name or idk havent searched too deep) 
    Also trying to build a habit of adding comments to classes to explain them  
    """

    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "user_data"

    class Config:
        json_schema_extra={
            "id": "4649e6c3-c228-4dc1-be63-8518fd53aacb",
            "name": "Matt",
            "email": "matt@example.com",
            "created_at": datetime.now()
        }
