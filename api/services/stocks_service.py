from util.stock_data import parse_table

def listings():
    table = parse_table()
    stocks = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        stock = {'symbol': columns[0].get_text(), 'name': columns[1].get_text()}
        stocks.append(stock)

    return stocks

def fetch_price(symbol):
    table = parse_table()
    for row in table.find_all('tr'):
        columns = row.find_all('td')

        if symbol.upper() == columns[0].get_text():
            return { 'price': float(columns[2].get_text().split()[0])}

    return {'price': None}
