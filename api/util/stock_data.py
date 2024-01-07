from bs4 import BeautifulSoup

url = 'https://www.pesobility.com/stock'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

async def fetch_data(session):
    async with session.get(url, headers=headers) as response:
        response.raise_for_status()
        return await response.text()
    
async def parse_table(session):
    html_content = await fetch_data(session)

    if not html_content:
        return None

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    return table

def parse_row(row):
    columns = row.find_all('td')
    return {'symbol': columns[0].get_text(), 'name': columns[1].get_text(), 'price': columns[2].get_text()}
