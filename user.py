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

def create_user(username, password):
    connection, cursor = establish_connection()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print(f"User with username '{username}' already exists. Please choose a different username.")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()

        cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        user_id = cursor.fetchone()

        cursor.execute("INSERT INTO portfolio (user_id, cash_balance, total_equities) VALUES (%s, 0, 0)", (user_id))
        connection.commit()

        print(f"User '{username}' created successfully!")

    close_connection(connection, cursor)

def login_user(username, password):
    connection, cursor = establish_connection()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    existing_user = cursor.fetchone()

    if existing_user:
        print(f"Login successful! Welcome, {username}!")
    else:
        print("Login failed. Please check your username and password.")

    close_connection(connection, cursor)

def delete_user(username):
    connection, cursor = establish_connection()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.execute("DELETE FROM users WHERE username = %s", (username,))
        connection.commit()
        print(f"User '{username}' deleted successfully!")
    else:
        print(f"User with username '{username}' not found.")

    close_connection(connection, cursor)


if __name__ == "__main__":
    print("[1] Log in")
    print("[2] Create account")
    print("[3] Delete account")
    print("[0] Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        login_user(username, password)

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        create_user(username, password)

    elif choice == "3":
        username = input("Enter username to delete: ")
        delete_user(username)

    elif choice == "0":
        print("Exiting the program.")

    else:
        print("Invalid choice. Please enter a valid option.")
