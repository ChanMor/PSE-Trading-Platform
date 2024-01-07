import aiohttp
import concurrent.futures
from util.stock_data import parse_table, parse_row

async def listings():
    async with aiohttp.ClientSession() as session:
        table = await parse_table(session)
        stocks = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_stock = {executor.submit(parse_row, row): row for row in table.find_all('tr')}
            
            for future in concurrent.futures.as_completed(future_to_stock):
                row = future_to_stock[future]
                try:
                    stock = future.result()
                    stocks.append(stock)
                except Exception as e:
                    print(f"Error processing row: {e}")

        return stocks

async def fetch_price(symbol):
    async with aiohttp.ClientSession() as session:
        table = await parse_table(session)

        table = parse_table()
        for row in table.find_all('tr'):
            columns = row.find_all('td')

            if symbol.upper() == columns[0].get_text():
                return { 'price': float(columns[2].get_text().split()[0])}

        return {'price': None}

