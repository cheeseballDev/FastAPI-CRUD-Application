from fastapi import APIRouter

user_router = APIRouter()

@user_router.post('/users')
async def create_user():
    pass

@user_router.get('/users/{user_id}')
async def get_user(user_id):
    pass

@user_router.put('/')
async def update_user():
    pass

@user_router.delete('/')
async def delete_user():
    pass