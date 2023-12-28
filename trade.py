import mysql.connector
import datetime
import queries as query

def establish_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='fcdm110503',
        database='trading_platform')
    cursor = connection.cursor()

    return connection, cursor

def close_connection(connection, cursor):
    connection.close()
    cursor.close()

def update_portfolio(user_id, transaction_type, total_shares, price):
    connection, cursor = establish_connection()

    update_portfolio_values = (total_shares * price, user_id)
    if transaction_type == 'BUY':
        update_portfolio_query = query.update_portfolio_buy_query
    else:
        update_portfolio_query = query.update_portfolio_sell_query
    
    cursor.execute(update_portfolio_query, update_portfolio_values)
    connection.commit()
    close_connection(connection, cursor)

def add_transaction(user_id, stock_symbol, transaction_type, total_shares, price):
    connection, cursor = establish_connection()

    transaction_date = datetime.datetime.now()

    transaction_values = (user_id, stock_symbol, transaction_type, total_shares, price, total_shares*price, transaction_date)
    cursor.execute(query.transaction_query, transaction_values)
    connection.commit()
       
    update_portfolio(user_id, transaction_type, total_shares, price)


    # update_stock_position_values = (user_id, stock_symbol, price, total_shares, price, total_shares * price, price, total_shares, total_shares, price, price)
    # cursor.execute(query.update_stock_position_query, update_stock_position_values)
    # connection.commit()

    close_connection(connection, cursor)


if __name__ == '__main__':
    add_transaction(10, 'ALI', 'BUY', 100, 5.5)