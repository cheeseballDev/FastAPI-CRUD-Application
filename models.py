from beanie import Document
from pydantic import Field
from datetime import datetime
import uuid

class User(Document):
    """
    User document for all data
    """
    id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    name: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "user_data"
