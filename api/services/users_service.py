from util.user_data import fetch_id, fetch_data

def fetch_user_id(username):
    return fetch_id(username)

def fetch_user_transactions(user_id):
    return fetch_data(user_id, "SELECT * FROM transactions WHERE user_id = %s")

def fetch_user_positions(user_id):
    return fetch_data(user_id, "SELECT * FROM positions WHERE user_id = %s")

def fetch_user_portfolio(user_id):
    return fetch_data(user_id, "SELECT * FROM portfolio WHERE user_id = %s")[0]




