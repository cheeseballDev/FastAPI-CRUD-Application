from typing import Optional
from beanie import Document
from pydantic import BaseModel, Field
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

class CreateNewUserRequest(BaseModel):
    """
    This model is used to pass data into the User document
    """
    name: str
    email: str

class UpdateUser(CreateNewUserRequest):
    """
    This model is used to update data into the User document, by using the 
    """
    name: Optional[str] = None
    email: Optional[str] = None

class CreateUserResponse(BaseModel):
    """
    This model is used to read the data in the User document
    """
    id: str
    name: str
    email: str
    created_at: datetime
