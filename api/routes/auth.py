from fastapi import APIRouter
import services.auth_service as au
from models.auth_model import CreateUserRequest, LoginUserRequest, DeleteUserRequest

router = APIRouter()    
    
@router.post('/login')
async def login_user_handler(request: LoginUserRequest):
    return au.login_user(request.username, request.password)

@router.post('')
async def create_user_handler(request: CreateUserRequest):
    return au.create_user(request.username, request.password)

@router.delete('')
async def delete_user_handler(request: DeleteUserRequest):
    return au.delete_user(request.username, request.password)
