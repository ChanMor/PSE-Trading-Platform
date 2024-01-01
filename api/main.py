from fastapi import FastAPI
from routes import stocks, auth, users, actions

app = FastAPI()

app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(stocks.router, prefix='/stocks', tags=['stocks'])
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(actions.router, prefix='/actions', tags=['actions'])
