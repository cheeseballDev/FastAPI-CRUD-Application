from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from uuid import UUID
from models import User, CreateNewUserRequest, CreateUserResponse
from typing import List

user_router = APIRouter()

@user_router.get('/api/users')
async def get_all_users() -> List[User]:
    all_users = await User.find_all().to_list()
    return all_users

@user_router.get('/api/users/{user_id}', response_model= User)
async def get_user(user_id: UUID=PydanticObjectId) -> User:
    user_to_get = await User.get(user_id)
    if user_to_get is None:
        raise HTTPException(status_code=404, detail="No user exists with that ID")
    return user_to_get

@user_router.post('/api/user', response_model= CreateUserResponse)
async def create_user(user_request: CreateNewUserRequest):
    new_user_document = User(name=user_request.name, email=user_request.email)
    await new_user_document.create()
    CreateUserResponse(id=new_user_document.id, name=new_user_document.name, email=new_user_document.email, created_at=new_user_document.created_at)
    return {"message":"User has been created", "user":CreateUserResponse}

@user_router.patch('/api/user/{user_id}', response_model= CreateUserResponse)
async def update_user(user_request: CreateNewUserRequest):
    user_to_update = User(user_request.name, user_request.email)
    if user_to_update is None:
        raise HTTPException(status_code = 404, detail = "No user exists with that ID")
    await user_to_update.update()
    return {"message": "Selected user has been updated", "user": User}

@user_router.delete('/api/user/{user_id}')
async def delete_user(user_id: UUID=PydanticObjectId):
    user_to_delete = await User.get(user_id)
    if user_to_delete is None:
        raise HTTPException(status_code = 404, detail = "No user exists with that ID")
    await user_to_delete.delete()
    return {"message": "Selected user has been deleted", "user": User}