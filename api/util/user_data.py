import util.database_manager as db

def fetch_data(user_id, query):
    connection, cursor = db.establish_connection()
    
    cursor.execute(query, (user_id,))    
    columns = [column[0] for column in cursor.description]

    items = cursor.fetchall()
    data = [dict(zip(columns, item)) for item in items]

    db.close_connection(connection, cursor)
    return data

def fetch_id(username):
    connection, cursor = db.establish_connection()

    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user_id_row = cursor.fetchone()
    
    db.close_connection(connection, cursor)
    return {'user_id': user_id_row[0]}

def cascade_user_deletion(user_id, username, cursor):
    cursor.execute("DELETE FROM portfolio WHERE user_id = %s", (user_id,))
    cursor.execute("DELETE FROM positions WHERE user_id = %s", (user_id,))
    cursor.execute("DELETE FROM transactions WHERE user_id = %s", (user_id,))
    cursor.execute("DELETE FROM users WHERE username = %s", (username,))