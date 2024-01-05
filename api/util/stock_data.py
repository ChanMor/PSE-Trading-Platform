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
    table = soup.find('table')
    return table