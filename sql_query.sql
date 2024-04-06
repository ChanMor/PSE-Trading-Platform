-- Create the database
CREATE DATABASE IF NOT EXISTS trading_platform;

-- Switch to the created database
USE trading_platform;

-- Create a table to store user information
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    );

-- Create a table to store stock information
CREATE TABLE IF NOT EXISTS stocks (
    symbol VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create a table to store transaction history
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    transaction_type ENUM('BUY', 'SELL') NOT NULL,
    total_shares INT NOT NULL,
    price DECIMAL(18, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create a table to store user balances and portfolio valuation
CREATE TABLE IF NOT EXISTS portfolio (
    user_id INT,
    cash_balance DECIMAL(18, 2) NOT NULL,
    total_equities DECIMAL(18, 2) NOT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create a table to store active stock positions
CREATE TABLE IF NOT EXISTS positions (
    user_id INT,
    symbol VARCHAR(10),
    average_price DECIMAL(18, 2) NOT NULL,
    total_shares INT NOT NULL,
    current_market_price DECIMAL(18, 2) NOT NULL,
    market_value DECIMAL(18, 2) NOT NULL,
    gain_loss DECIMAL(18, 2) NOT NULL,
    percentage_gain_loss DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY (user_id, symbol),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (symbol) REFERENCES stocks(symbol)
);

SELECT *from transactions;
ALTER TABLE transactions
ADD gross_amount DECIMAL(18, 2) NOT NULL;