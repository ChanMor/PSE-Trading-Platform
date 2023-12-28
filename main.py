from fastapi import FastAPI
from fastapi import HTTPException
import stocks as st
import fetch_database as fd

app = FastAPI()

@app.get('/listings')
async def listings():
    return st.listings()\
    
@app.get('/stock-price/{stock}')
async def price(stock: str):
    return st.fetch_price(stock)


@app.get('/{username}/transaction-history')
async def price(username: str):
    try:
        return fd.fetch_user_transactions(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


