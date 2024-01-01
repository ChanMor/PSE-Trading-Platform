url = 'https://www.pesobility.com/stock'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

transaction_query = (
    "INSERT INTO transactions (user_id, symbol, transaction_type, "
    "total_shares, price, gross_amount, transaction_date) VALUES "
    "(%s, %s, %s, %s, %s, %s, %s)")

update_portfolio_buy_query = (
    "UPDATE portfolio SET cash_balance = cash_balance - %s "
    "WHERE user_id = %s")

update_portfolio_sell_query = (
    "UPDATE portfolio SET cash_balance = cash_balance + %s "
    "WHERE user_id = %s")

position_query = (
    "INSERT INTO positions (user_id, symbol, average_price, total_shares, "
    "current_market_price, market_value, gain_loss, percentage_gain_loss) VALUES "
    "(%s, %s, %s, %s, %s, %s, 0, 0) "
    "ON DUPLICATE KEY UPDATE "
    "average_price = ((average_price * total_shares) + (%s * %s)) / (total_shares + %s), "
    "total_shares = total_shares + %s, "
    "current_market_price = %s, "
    "market_value = total_shares * %s")


