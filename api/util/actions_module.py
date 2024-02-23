import datetime
import util.database_manager as db
from util.queries import buy_position_query, sell_position_query, transaction_query

def authenticate_user(username, password):
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    existing_user = cursor.fetchone()

    db.close_connection(connection, cursor)
    return existing_user

def authenticate_user_id(user_id):
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    existing_user = cursor.fetchone()
    
    db.close_connection(connection, cursor)
    return existing_user

def get_cash_balance(user_id):
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT cash_balance FROM portfolio WHERE user_id = %s", (user_id,))
    cash_balance = cursor.fetchone()

    db.close_connection(connection, cursor)
    return cash_balance

def update_cash_balance(user_id, amount):
    connection, cursor = db.establish_connection()

    cursor.execute("UPDATE portfolio SET cash_balance = cash_balance + %s WHERE user_id = %s", (amount, user_id))
    connection.commit()

    db.close_connection(connection, cursor)

def update_position(transaction, user_id, stock_symbol, total_shares, price):
    connection, cursor = db.establish_connection()

    if transaction == 'BUY':
        position_values = (user_id, stock_symbol, price, total_shares, price, total_shares * price, price, total_shares, total_shares, total_shares, price, price, price, price)
        cursor.execute(buy_position_query, position_values)

    if transaction == 'SELL':
        position_values = (total_shares, price, price, price, user_id, stock_symbol)
        cursor.execute(sell_position_query, position_values)

    connection.commit()
    db.close_connection(connection, cursor)


def update_transaction(transaction, user_id, stock_symbol, total_shares, price, amount):
    connection, cursor = db.establish_connection()
    transaction_date = datetime.datetime.now()

    if transaction == 'BUY':
        transaction_values = (user_id, stock_symbol, 'BUY', total_shares, price, total_shares*price, transaction_date)
        cursor.execute(transaction_query, transaction_values)

    if transaction == 'SELL':
        transaction_values = (user_id, stock_symbol, 'SELL', total_shares, price, amount, transaction_date)
        cursor.execute(transaction_query, transaction_values)

    connection.commit()
    db.close_connection(connection, cursor)
