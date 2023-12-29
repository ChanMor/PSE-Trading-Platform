import database_manager as db

def delete(query):
    connection, cursor = db.establish_connection()
    cursor.execute(query)
    connection.commit()
    db.close_connection(connection, cursor)

def clear_transactions():
    delete("DELETE FROM transactions")

def clear_positions():
    delete("DELETE FROM positions")

def clear_portfolio():
    delete("DELETE FROM portfolio")

def clear_users():
    delete("DELETE FROM users")

def clear_stocks():
    delete("DELETE FROM stocks")

def clear_database():
    clear_transactions()
    clear_positions()
    clear_portfolio()
    clear_users()
    clear_stocks()
