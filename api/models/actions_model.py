from pydantic import BaseModel
from decimal import Decimal

class UpdateUsernameRequest(BaseModel):
    username: str
    password: str
    new_username: str

class UpdatePasswordRequest(BaseModel):
    username: str
    password: str
    new_password: str

class BalanceRequest(BaseModel):
    user_id: int
    amount: Decimal

class BuyRequest(BaseModel):
    user_id: int
    stock_symbol: str
    total_shares: int
    price: Decimal


