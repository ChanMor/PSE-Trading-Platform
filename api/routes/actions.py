from fastapi import APIRouter
import services.actions_service as ac
from models.actions_model import UpdateUsernameRequest, UpdatePasswordRequest, BalanceRequest, TransactionRequest

router = APIRouter()   

@router.post('/update/username')
async def update_username(request: UpdateUsernameRequest):
    return ac.update_username(request.username, request.password, request.new_username)

@router.post('/update/password')
async def update_password(request: UpdatePasswordRequest):
    return ac.update_password(request.username, request.password, request.new_password)

@router.post('/update/data')
async def update():
    return ac.update_data()

@router.post('/deposit')
async def deposit(request: BalanceRequest):
    return ac.deposit(request.user_id, request.amount)

@router.post('/withdraw')
async def withdraw(request: BalanceRequest):
    return ac.withdraw(request.user_id, request.amount)

@router.post('/buy')
async def buy(request: TransactionRequest):
    return ac.buy(request.user_id, request.stock_symbol, request.shares)

@router.post('/sell')
async def sell(request: TransactionRequest):
    return ac.sell(request.user_id, request.stock_symbol, request.shares)

