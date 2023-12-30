from fastapi import FastAPI
from routes import stocks, users

app = FastAPI()

app.include_router(stocks.router, prefix='/stocks', tags=['stocks'])
app.include_router(users.router, prefix='/users', tags=['users'])
