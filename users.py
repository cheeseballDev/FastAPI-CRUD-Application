from fastapi import APIRouter

user_router = APIRouter()

@user_router.post('api/users')
async def create_user():
    pass

@user_router.get('api/users/{user_id}')
async def get_user(user_id):
    pass

@user_router.patch('api/users/{user_id}')
async def update_user():
    pass

@user_router.delete('api/userr/{user_id}')
async def delete_user(user_id):
    pass