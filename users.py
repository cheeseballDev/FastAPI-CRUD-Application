from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from uuid import UUID
from models import User
from typing import List

user_router = APIRouter()

@user_router.get('/api/users/{user_id}', response_model=User)
async def get_user(user_id: UUID=PydanticObjectId) -> List[User]:
    user = await User.find_one(User.id == user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="No user exists with that ID")
    return user

@user_router.post('/api/users')
async def create_user(user:User):
    await user.create()
    return {"message":"User has been created"}

@user_router.patch('/api/users/{user_id}')
async def update_user(user_id: UUID = PydanticObjectId):

    return user

@user_router.delete('/api/userr/{user_id}')
async def delete_user(user_id):
    pass