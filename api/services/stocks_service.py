# from util.stock_data import parse_table

# def listings():
#     table = parse_table()
#     stocks = []
#     for row in table.find_all('tr'):
#         columns = row.find_all('td')
#         stock = {'symbol': columns[0].get_text(), 'name': columns[1].get_text(), 'price': columns[2].get_text()}
#         stocks.append(stock)

#     return stocks

# def fetch_price(symbol):
#     table = parse_table()

#     for row in table.find_all('tr'):
#         columns = row.find_all('td')

#         if symbol.upper() == columns[0].get_text():
#             return { 'price': float(columns[2].get_text().split()[0])}

#     return {'price': None}


import requests
from bs4 import BeautifulSoup

url = 'https://www.pesobility.com/stock'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def fetch_data():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_table():
    html_content = fetch_data()

    if not html_content:
        return None

    soup = BeautifulSoup(html_content, 'html.parser')
    target_div = soup.find('div', class_='large-12 columns')

    if not target_div:
        return None

    table = target_div.find('table')
    return table


def listings():
    table = parse_table()
    stocks = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        stock = {'symbol': columns[0].get_text(), 'name': columns[1].get_text(), 'price': columns[2].get_text()}
        stocks.append(stock)

    return stocks

def fetch_price(symbol):
    table = parse_table()

    for row in table.find_all('tr'):
        columns = row.find_all('td')

        if symbol.upper() == columns[0].get_text():
            return { 'price': float(columns[2].get_text().split()[0])}

    return {'price': None}

