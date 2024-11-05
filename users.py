from fastapi import APIRouter
from models import User
from typing import List

user_router = APIRouter()

@user_router.get('/api/users/{user_id}')
async def get_user(user_id) -> List[User]:
    user = await User.find_all().to_list()
    return user

@user_router.post('/api/users')
async def create_user(user:User):
    await user.create()
    return {"message":"User has been created"}

@user_router.patch('/api/users/{user_id}')
async def update_user():
    pass

@user_router.delete('/api/userr/{user_id}')
async def delete_user(user_id):
    pass