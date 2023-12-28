import mysql.connector

def fetch_user_transactions(username):
    
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='fcdm110503',
        database='trading_platform')
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user_id_dict = cursor.fetchone()

    if not user_id_dict:
        return None

    user_id = user_id_dict['user_id']
    cursor.execute("SELECT * FROM transactions WHERE user_id = %s", (user_id,))
    transactions = cursor.fetchall()

    cursor.close()
    connection.close()
    return transactions


if __name__ == '__main__':
    print(fetch_user_transactions('user1'))
