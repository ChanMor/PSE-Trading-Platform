import mysql.connector

class User:
    connection = None
    cursor = None

    @staticmethod
    def establish_connection():
        User.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='fcdm110503',
            database='trading_platform')
        User.cursor = User.connection.cursor()

    @staticmethod
    def close_connection():
        User.cursor.close()
        User.connection.close()

    @staticmethod
    def create_user(username, password):
        User.establish_connection()
        User.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = User.cursor.fetchone()

        if existing_user:
            print(f"User with username '{username}' already exists. Please choose a different username.")
        else:
            User.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            User.connection.commit()
            print(f"User '{username}' created successfully!")

        User.close_connection()

    @staticmethod
    def login_user(username, password):
        User.establish_connection()
        User.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        existing_user = User.cursor.fetchone()

        if existing_user:
            print(f"Login successful! Welcome, {username}!")
        else:
            print("Login failed. Please check your username and password.")

        User.close_connection()

    @staticmethod
    def delete_user(username):
        User.establish_connection()
        User.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = User.cursor.fetchone()

        if existing_user:
            User.cursor.execute("DELETE FROM users WHERE username = %s", (username,))
            User.connection.commit()
            print(f"User '{username}' deleted successfully!")
        else:
            print(f"User with username '{username}' not found.")

        User.close_connection()






if __name__ == "__main__":
    print("[1] Log in")
    print("[2] Create account")
    print("[3] Delete account")
    print("[0] Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        User.login_user(username, password)

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        User.create_user(username, password)

    elif choice == "3":
        username = input("Enter username to delete: ")
        User.delete_user(username)

    elif choice == "0":
        print("Exiting the program.")

    else:
        print("Invalid choice. Please enter a valid option.")
