import util.database_manager as db
import util.actions_module as am
import services.stocks_service as st


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


def buy(user_id, stock_symbol, total_shares):
    connection, cursor = db.establish_connection()

    price = st.fetch_price(stock_symbol)['price']

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

    current_market_price = st.fetch_price(stock_symbol)['price']

    cursor.execute("SELECT total_shares FROM positions WHERE user_id = %s AND symbol = %s", (user_id, stock_symbol,))
    total_shares = cursor.fetchone()

    amount = shares * current_market_price

    if not total_shares or total_shares[0] < shares:
        db.close_connection(connection, cursor)
        return {"message": "Transaction failed. Insufficient shares!"}

    am.update_cash_balance(user_id, amount)

    if total_shares[0] == shares:
        cursor.execute("DELETE FROM positions WHERE user_id = %s AND symbol = %s", (user_id, stock_symbol,))
        connection.commit()
    else:
        am.update_position('SELL', user_id, stock_symbol, shares, current_market_price)
        am.update_transaction('SELL', user_id, stock_symbol, shares, current_market_price, amount)

    db.close_connection(connection, cursor)
    return {"message": f"Successfully sold {shares} shares of {stock_symbol}!"}

def update_data():
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT user_id, symbol, average_price, total_shares FROM positions")
    positions = cursor.fetchall()

    for position in positions:
        user_id, symbol, average_price, total_shares = position

        latest_price = st.fetch_price(symbol)['price']

        market_value = total_shares * latest_price
        gain_loss = (total_shares * latest_price) - (average_price * total_shares)  
        percentage_gain_loss = ((total_shares * latest_price) - (average_price * total_shares)) / (average_price * total_shares) * 100  

        cursor.execute("UPDATE positions SET current_market_price = %s, market_value = %s, gain_loss = %s, percentage_gain_loss = %s WHERE user_id = %s AND symbol = %s",
                       (latest_price, market_value, gain_loss, percentage_gain_loss, user_id, symbol))

    connection.commit()
    db.close_connection(connection, cursor)

