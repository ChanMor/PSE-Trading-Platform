from fastapi import APIRouter
import models.user_model as um
from util.user_model import CreateUserRequest, LoginUserRequest, DeleteUserRequest

router = APIRouter()    

@router.get('/{username}/user_id')
async def get_user_id(username: str):
    return um.fetch_user_id(username)

@router.get('/{user_id}/transaction-history')
async def get_user_transactions(user_id: str):
    return um.fetch_user_transactions(user_id)

@router.get('/{user_id}/stock-positions')
async def price(user_id: str):
    return um.fetch_user_positions(user_id)

@router.get('/{user_id}/portfolio')
async def price(user_id: str):
    return um.fetch_user_portfolio(user_id)

@router.post('/login-user')
async def login_user_handler(request: LoginUserRequest):
    return um.login_user(request.username, request.password)

@router.post('/create-user')
async def create_user_handler(request: CreateUserRequest):
    return um.create_user(request.username, request.password)

@router.delete('/delete-user')
async def delete_user_handler(request: DeleteUserRequest):
    return um.delete_user(request.username, request.password)




