from fastapi import FastAPI
import stocks as st
import database_scripts.fetch_database as fd

app = FastAPI()

@app.get('/listings')
async def listings():
    return st.listings()
    
@app.get('/stock-price/{stock}')
async def price(stock: str):
    return st.fetch_price(stock)

@app.get('/{username}/user_id')
async def price(username: str):
    return fd.fetch_user_id(username)

@app.get('/{user_id}/transaction-history')
async def price(user_id: str):
    return fd.fetch_user_transactions(user_id)

@app.get('/{user_id}/stock-positions')
async def price(user_id: str):
    return fd.fetch_user_positions(user_id)

@app.get('/{user_id}/portfolio')
async def price(user_id: str):
    return fd.fetch_user_portfolio(user_id)




