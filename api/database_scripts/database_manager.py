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