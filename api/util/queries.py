
transaction_query = (
    "INSERT INTO transactions (user_id, symbol, transaction_type, "
    "total_shares, price, gross_amount, transaction_date) VALUES "
    "(%s, %s, %s, %s, %s, %s, %s)"
)

update_portfolio_buy_query = (
    "UPDATE portfolio SET cash_balance = cash_balance - %s "
    "WHERE user_id = %s"
)

update_portfolio_sell_query = (
    "UPDATE portfolio SET cash_balance = cash_balance + %s "
    "WHERE user_id = %s"
)

buy_position_query = (
    "INSERT INTO positions (user_id, symbol, average_price, total_shares, "
    "current_market_price, market_value, gain_loss, percentage_gain_loss) VALUES "
    "(%s, %s, %s, %s, %s, %s, 0, 0) "
    "ON DUPLICATE KEY UPDATE "
    "average_price = ((average_price * total_shares) + (%s * %s)) / (total_shares + %s), "
    "total_shares = total_shares + %s, "
    "current_market_price = %s, "
    "market_value = total_shares * %s, "
    "gain_loss = (total_shares * %s) - (average_price * total_shares), "
    "percentage_gain_loss = ((total_shares * %s) - (average_price * total_shares)) / (average_price * total_shares) * 100 "
)
    

sell_position_query = (
    "UPDATE positions SET "
    "total_shares = total_shares - %s, "
    "market_value = total_shares * %s, "
    "gain_loss = (total_shares * %s) - (average_price * total_shares), "
    "percentage_gain_loss = ((total_shares * %s) - (average_price * total_shares)) / (average_price * total_shares) * 100 "
    "WHERE user_id = %s AND symbol = %s"
)
