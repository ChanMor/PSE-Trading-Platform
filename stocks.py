import requests
from bs4 import BeautifulSoup

class Stocks:
    BASE_URL = 'https://www.pesobility.com/stock'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    @staticmethod
    def fetch_data():
        try:
            response = requests.get(Stocks.BASE_URL, headers=Stocks.HEADERS)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    @staticmethod
    def listings():
        html_content = Stocks.fetch_data()
        if not html_content:
            return None

        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table')

        stocks = []
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            stock = {'symbol': columns[0].get_text(strip=True), 'name': columns[1].get_text(strip=True)}
            stocks.append(stock)

        return stocks
    
    @staticmethod
    def get_price(symbol):
        html_content = Stocks.fetch_data()
        if not html_content:
            return None

        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table') 

        for row in table.find_all('tr'):
            columns = row.find_all('td')
            
            if symbol.upper() == columns[0].get_text(strip=True):
                return columns[2].get_text(strip=True).split()[0]

        return None

if __name__ == '__main__':


    print("[1] print all stocks")
    print("[2] get stock price")
    
    choice = input("enter choice: ")

    if choice == '1':
        stocks_data = Stocks.listings()
        print(stocks_data)

    elif choice == '2':
        symbol = input("enter symbol: ")
        print(Stocks.get_price(symbol))
    