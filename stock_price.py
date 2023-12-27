import time
import requests
from bs4 import BeautifulSoup

def get_stock_price(ticker):

    url = f'https://frames.pse.com.ph/security/{ticker}'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
    time.sleep(1)

    soup = BeautifulSoup(response.text, 'html.parser')
        
    stock_price_element = soup.find('h3', {"class": "last-price"})
    
    if stock_price_element:
        stock_price = stock_price_element.text.strip()
        return stock_price
    else:
        return None

if __name__ == "__main__":
    ticket = input("Enter ticker: ")
    stock_price = get_stock_price(ticket)
    if stock_price != None:
        print(float(stock_price))
    else:
        print("NA")


