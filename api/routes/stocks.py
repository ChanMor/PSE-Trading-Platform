from fastapi import APIRouter
import services.stocks_service as st

router = APIRouter()

@router.get('/listings')
async def listings():
    return st.listings()

@router.get('/price/{symbol}')
async def price(symbol: str):
    return st.fetch_price(symbol)
