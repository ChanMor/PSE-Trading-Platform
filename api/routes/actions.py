from fastapi import APIRouter
import services.actions_service as ac
from models.actions_model import UpdateUsernameRequest, UpdatePasswordRequest, BalanceRequest

router = APIRouter()   

@router.post('/update/username')
async def update_username(request: UpdateUsernameRequest):
    return ac.update_username(request.username, request.password, request.new_username)

@router.post('/update/password')
async def update_password(request: UpdatePasswordRequest):
    return ac.update_password(request.username, request.password, request.new_password)

@router.post('/deposit')
async def deposit(request: BalanceRequest):
    return ac.deposit(request.user_id, request.amount)

@router.post('/withdraw')
async def withdraw(request: BalanceRequest):
    return ac.withdraw(request.user_id, request.amount)
