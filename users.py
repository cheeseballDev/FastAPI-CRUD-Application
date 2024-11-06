from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from uuid import UUID
from models import User
from typing import List

user_router = APIRouter()

@user_router.get('/api/users')
async def get_all_users() -> List[User]:
    all_users = await User.find_all().to_list()
    return all_users

@user_router.get('/api/users/{user_id}', response_model= User)
async def get_user(user_id: UUID=PydanticObjectId) -> User:
    user_to_get = await User.find_one(User.id == user_id)
    if user_to_get is None:
        raise HTTPException(status_code=404, detail="No user exists with that ID")
    return user_to_get

@user_router.post('/api/user')
async def create_user(user: User):
    await user.create()
    return {"message":"User has been created"}

@user_router.patch('/api/user/{user_id}', response_model= User)
async def update_user(user_id: UUID=PydanticObjectId, name: User=PydanticObjectId, email: User=PydanticObjectId):
    user_to_update = await User.find_one(User.id == user_id)
    if user_to_update is None:
        raise HTTPException(status_code = 404, detail = "No user exists with that ID")
    await user_to_update.update(name, email)
    return {"message": "Selected user has been updated"}

@user_router.delete('/api/user/{user_id}')
async def delete_user(user_id: UUID=PydanticObjectId):
    user_to_delete = await User.find_one(User.id == user_id)
    if user_to_delete is None:
        raise HTTPException(status_code = 404, detail = "No user exists with that ID")
    await user_to_delete.delete()
    return {"message": "Selected user has been deleted"}