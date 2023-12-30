import util.database_manager as db

def cascade_user_deletion(user_id, username, cursor):
    cursor.execute("DELETE FROM portfolio WHERE user_id = %s", (user_id,))
    cursor.execute("DELETE FROM positions WHERE user_id = %s", (user_id,))
    cursor.execute("DELETE FROM transactions WHERE user_id = %s", (user_id,))
    cursor.execute("DELETE FROM users WHERE username = %s", (username,))

def fetch_user_id(username):
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user_id_row = cursor.fetchone()
    
    db.close_connection(connection, cursor)
    return {'user_id': user_id_row[0]}

def fetch_data(user_id, query):
    connection, cursor = db.establish_connection()
    
    cursor.execute(query, (user_id,))    
    columns = [column[0] for column in cursor.description]

    items = cursor.fetchall()
    data = [dict(zip(columns, item)) for item in items]

    db.close_connection(connection, cursor)
    return data

def fetch_user_transactions(user_id):
    return fetch_data(user_id, "SELECT * FROM transactions WHERE user_id = %s")

def fetch_user_positions(user_id):
    return fetch_data(user_id, "SELECT * FROM positions WHERE user_id = %s")

def fetch_user_portfolio(user_id):
    return fetch_data(user_id, "SELECT * FROM portfolio WHERE user_id = %s")[0]


def create_user(username, password):
    connection, cursor = db.establish_connection()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        db.close_connection(connection, cursor)
        return {'message': 'User already exist!'}
    
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    connection.commit()

    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user_id = cursor.fetchone()

    cursor.execute("INSERT INTO portfolio (user_id, cash_balance, total_equities) VALUES (%s, 0, 0)", (user_id))
    
    connection.commit()
    db.close_connection(connection, cursor)
    return {"message": "User created successfully!"}


def login_user(username, password):
    connection, cursor = db.establish_connection()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    existing_user = cursor.fetchone()

    if existing_user:
        db.close_connection(connection, cursor)
        return {"message": "User login successfully!"}
    
    db.close_connection(connection, cursor)
    return {"message": "Login failed. Check username and password!"}

def delete_user(username, password):
    connection, cursor = db.establish_connection()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    existing_user = cursor.fetchone()

    if not existing_user:
        db.close_connection(connection, cursor)
        return {"message": "Deletion failed. Check username and password!"}
    
    user_id = existing_user[0]
    cascade_user_deletion(user_id, username, cursor)

    connection.commit()
    db.close_connection(connection, cursor)
    return {"message": "User deleted successfully!"}
