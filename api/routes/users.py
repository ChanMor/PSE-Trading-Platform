from fastapi import APIRouter
import models.user_model as um

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





