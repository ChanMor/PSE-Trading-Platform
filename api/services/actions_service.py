import util.database_manager as db
import datetime

from util.queries import transaction_query, position_query


def update_username(username, password, new_username):
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    existing_user = cursor.fetchone()

    if not existing_user:
        db.close_connection(connection, cursor)
        return {"message": "Invalid username or password!"}

    cursor.execute("UPDATE users SET username = %s WHERE username = %s AND password = %s", (new_username, username, password))
    connection.commit()

    db.close_connection(connection, cursor)
    return {"message": "Username updated successfully!"}

def update_password(username, password, new_password):
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    existing_user = cursor.fetchone()

    if not existing_user:
        db.close_connection(connection, cursor)
        return {"message": "Invalid username or password!"}

    cursor.execute("UPDATE users SET password = %s WHERE username = %s AND password = %s", (new_password, username, password))
    connection.commit()

    db.close_connection(connection, cursor)
    return {"message": "Password updated successfully!"}

def deposit(user_id, amount):
    if amount < 0:
        return {"message": "Invalid deposit amount!"}

    connection, cursor = db.establish_connection()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        db.close_connection(connection, cursor)
        return {"message": "User not found!"}

    cursor.execute("UPDATE portfolio SET cash_balance = cash_balance + %s, total_equities = total_equities + %s WHERE user_id = %s", (amount, amount, user_id))
    connection.commit()

    db.close_connection(connection, cursor)
    return {"message": f"Deposited {amount} successfully!"}

def withdraw(user_id, amount):
    if amount < 0:
        return {"message": "Invalid withdraw amount!"}
    
    connection, cursor = db.establish_connection()
    cursor.execute("SELECT cash_balance FROM portfolio WHERE user_id = %s", (user_id,))
    cash_balance = cursor.fetchone()

    if not cash_balance:
        db.close_connection(connection, cursor)
        return {"message": "User not found!"}

    if cash_balance[0] < amount:
        db.close_connection(connection, cursor)
        return {"message": "Withdrawal failed. Insufficient balance!"}

    cursor.execute("UPDATE portfolio SET cash_balance = cash_balance - %s, total_equities = total_equities - %s WHERE user_id = %s", (amount, amount, user_id))
    connection.commit()

    db.close_connection(connection, cursor)
    return {"message": f"Withdrawn {amount} successfully!"}


def buy(user_id, stock_symbol, total_shares, price):
    connection, cursor = db.establish_connection()
    amount = total_shares * price

    cursor.execute("SELECT cash_balance FROM portfolio WHERE user_id = %s", (user_id,))
    cash_balance = cursor.fetchone()

    if not cash_balance:
        db.close_connection(connection, cursor)
        return {"message": "User not found!"}

    if cash_balance[0] < amount:
        db.close_connection(connection, cursor)
        return {"message": "Transaction failed. Insufficient balance!"}

    cursor.execute("UPDATE portfolio SET cash_balance = cash_balance - %s WHERE user_id = %s", (amount, user_id))
    connection.commit()

    position_values = (user_id, stock_symbol, price, total_shares, price, total_shares * price, price, total_shares, total_shares, total_shares, price, price)
    cursor.execute(position_query, position_values)
    connection.commit()

    transaction_date = datetime.datetime.now()
    transaction_values = (user_id, stock_symbol, 'buy', total_shares, price, total_shares*price, transaction_date)
    cursor.execute(transaction_query, transaction_values)
    connection.commit()

    db.close_connection(connection, cursor)
    return {"message": f"Successfully bought {total_shares} shares of {stock_symbol}!"}

def sell(user_id, stock_symbol, total_shares, price):
    return
def update_data():
    return
