from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from models import UpdateUser, User, CreateNewUserRequest, CreateUserResponse
from typing import Dict, List, Union

user_router = APIRouter()

@user_router.get('/api/users')
async def get_all_users() -> List[User]:
    all_users = await User.find_all().to_list()
    return all_users

@user_router.get('/api/user/{user_id}', response_model= CreateUserResponse)
async def get_user(user_id) -> User:
    user = await User.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="No user exists with that ID")
    return user

@user_router.post('/api/user', response_model=Dict[str, Union[str, CreateUserResponse]])
async def create_user(user_request: CreateNewUserRequest) -> any:
    new_user = User(name=user_request.name, email=user_request.email)
    await new_user.create()
    return {
        "message":"User has been created", 
        "user": CreateUserResponse(
            id=new_user.id,
            name=new_user.name,
            email=new_user.email,
            created_at=new_user.created_at
        )
    }

@user_router.patch('/api/user/{user_id}', response_model=Dict[str, Union[str, CreateUserResponse]])
async def update_user(user_id, user_request: UpdateUser) -> any:
    user = await User.get(user_id)
    if user_request.name:
        user.name = user_request.name
    if user_request.email:
        user.email = user_request.email
    await user.save()
    return {
        "message": "User has been updated",
        "User": CreateUserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at
        )
    }

@user_router.delete('/api/user/{user_id}')
async def delete_user(user_id) -> str:
    user_to_delete = await User.get(user_id)
    if user_to_delete is None:
        raise HTTPException(status_code = 404, detail = "No user exists with that ID")
    await user_to_delete.delete()
    return {"message": "User has been deleted"}