import util.database_manager as db
import util.actions_module as am


def update_username(username, password, new_username):
    connection, cursor = db.establish_connection()

    if not am.authenticate_user(username, password):
        db.close_connection(connection, cursor)
        return {"message": "Invalid username or password!"}

    cursor.execute("UPDATE users SET username = %s WHERE username = %s AND password = %s", (new_username, username, password))
    connection.commit()

    db.close_connection(connection, cursor)
    return {"message": "Username updated successfully!"}

def update_password(username, password, new_password):
    connection, cursor = db.establish_connection()

    if not am.authenticate_user(username, password):
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

    if not am.authenticate_user_id(user_id):
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

    cash_balance = am.get_cash_balance(user_id)

    if not cash_balance or cash_balance[0] < amount:
        db.close_connection(connection, cursor)
        return {"message": "Withdrawal failed. Insufficient balance!"}

    cursor.execute("UPDATE portfolio SET cash_balance = cash_balance - %s, total_equities = total_equities - %s WHERE user_id = %s", (amount, amount, user_id))
    connection.commit()

    db.close_connection(connection, cursor)
    return {"message": f"Withdrawn {amount} successfully!"}


def buy(user_id, stock_symbol, total_shares, price):
    connection, cursor = db.establish_connection()

    amount = total_shares * price
    cash_balance = am.get_cash_balance(user_id)

    if not cash_balance or cash_balance[0] < amount:
        db.close_connection(connection, cursor)
        return {"message": "Transaction failed. Insufficient balance!"}

    am.update_cash_balance(user_id, -1*amount)
    am.update_position('BUY', user_id, stock_symbol, total_shares, price)
    am.update_transaction('BUY', user_id, stock_symbol, total_shares, price, None)


    db.close_connection(connection, cursor)
    return {"message": f"Successfully bought {total_shares} shares of {stock_symbol}!"}

def sell(user_id, stock_symbol, shares):
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT current_market_price FROM positions WHERE user_id = %s AND symbol = %s", (user_id, stock_symbol,))
    current_market_price = cursor.fetchone()

    cursor.execute("SELECT total_shares FROM positions WHERE user_id = %s AND symbol = %s", (user_id, stock_symbol,))
    total_shares = cursor.fetchone()

    if not total_shares or total_shares[0] < shares:
        db.close_connection(connection, cursor)
        return {"message": "Transaction failed. Insufficient shares!"}

    amount = shares * current_market_price[0]

    am.update_cash_balance(user_id, amount)
    am.update_position('SELL', user_id, stock_symbol, shares, current_market_price)
    am.update_transaction('SELL', user_id, stock_symbol, shares, current_market_price, amount)

    db.close_connection(connection, cursor)
    return {"message": f"Successfully sold {shares} shares of {stock_symbol}!"}


def update_data():
    return
