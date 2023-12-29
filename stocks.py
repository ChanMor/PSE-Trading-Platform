import requests
from bs4 import BeautifulSoup

from queries import url, headers


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
    table = soup.find('table')
    return table

def listings():
    table = parse_table()

    stocks = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        stock = {'symbol': columns[0].get_text(strip=True), 'name': columns[1].get_text(strip=True)}
        stocks.append(stock)

    return stocks

def fetch_price(symbol):
    table = parse_table()

    for row in table.find_all('tr'):
        columns = row.find_all('td')

        if symbol.upper() == columns[0].get_text(strip=True):
            return { 'price': float(columns[2].get_text(strip=True).split()[0])}

    return {'price': None}
