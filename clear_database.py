import mysql.connector

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

def clear_transactions():
    connection, cursor = establish_connection()
    cursor.execute("DELETE FROM transactions")
    connection.commit()
    close_connection(connection, cursor)

def clear_positions():
    connection, cursor = establish_connection()
    cursor.execute("DELETE FROM positions")
    connection.commit()
    close_connection(connection, cursor)

def clear_portfolio():
    connection, cursor = establish_connection()
    cursor.execute("DELETE FROM portfolio")
    connection.commit()
    close_connection(connection, cursor)

def clear_users():
    connection, cursor = establish_connection()
    cursor.execute("DELETE FROM users")
    connection.commit()
    close_connection(connection, cursor)

def clear_stocks():
    connection, cursor = establish_connection()
    cursor.execute("DELETE FROM stocks")
    connection.commit()
    close_connection(connection, cursor)