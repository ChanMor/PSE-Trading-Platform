from fastapi import APIRouter
import services.users_service as ur

router = APIRouter()

@router.get('/{username}/user_id')
async def user_id(username: str):
    return ur.fetch_user_id(username)

@router.get('/{user_id}/transaction')
async def user_transactions(user_id: str):
    return ur.fetch_user_transactions(user_id)

@router.get('/{user_id}/positions')
async def user_positions(user_id: str):
    return ur.fetch_user_positions(user_id)

@router.get('/{user_id}/portfolio')
async def user_portfolio(user_id: str):
    return ur.fetch_user_portfolio(user_id)
