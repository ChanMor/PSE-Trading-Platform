from fastapi import APIRouter
import models.stock_model as sm

router = APIRouter()

@router.get('/listings')
async def listings():
    return sm.listings()

@router.get('/price/{symbol}')
async def price(symbol: str):
    return sm.fetch_price(symbol)
