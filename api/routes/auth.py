from fastapi import APIRouter
import models.auth_model as am
from util.auth_model import CreateUserRequest, LoginUserRequest, DeleteUserRequest

router = APIRouter()    


@router.post('/login')
async def login_user_handler(request: LoginUserRequest):
    return am.login_user(request.username, request.password)

@router.post('')
async def create_user_handler(request: CreateUserRequest):
    return am.create_user(request.username, request.password)

@router.delete('')
async def delete_user_handler(request: DeleteUserRequest):
    return am.delete_user(request.username, request.password)
