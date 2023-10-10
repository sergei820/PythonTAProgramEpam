import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json


async def fetch_company_data(session, url):
    async with session.get(url) as response:
        return await response.text()


async def parse_company_data(session, company_url, companies_data):
    company_page = await fetch_company_data(session, company_url)
    soup = BeautifulSoup(company_page, 'html.parser')

    # Parse the required information from the company page
    company_name = soup.find('h1', class_='price-section__name').text.strip()
    company_code = soup.find('span', class_='price-section__label').text.strip()
    company_price = soup.find('div', class_='price-section__current-value').text.strip()
    company_pe = soup.find('span', text='P/E Ratio').find_next('span').text.strip()
    company_growth = soup.find('span', text='1 Year Return').find_next('span').text.strip()

    # Create a dictionary for the company
    company_info = {
        'code': company_code,
        'name': company_name,
        'price': company_price,
        'P/E': company_pe,
        'growth': company_growth,
    }

    companies_data.append(company_info)


async def main():
    base_url = 'https://markets.businessinsider.com'
    sp500_url = f'{base_url}/index/components/s&p_500'

    async with aiohttp.ClientSession() as session:
        response = await fetch_company_data(session, sp500_url)
        soup = BeautifulSoup(response, 'html.parser')
        company_links = [a['href'] for a in soup.select('tbody.table__tbody tr td:nth-child(1) a')]

        tasks = []
        companies_data = []

        for link in company_links:
            company_url = base_url + link
            task = asyncio.ensure_future(parse_company_data(session, company_url, companies_data))
            tasks.append(task)

        await asyncio.gather(*tasks)

        # Sort companies by price, P/E, and growth and select the top 10
        top_10_price = sorted(companies_data, key=lambda x: float(x['price'].replace(',', '').replace('$', '')), reverse=True)[:10]
        top_10_pe = sorted(companies_data, key=lambda x: float(x['P/E'].replace(',', '').replace('x', '')))[:10]
        top_10_growth = sorted(companies_data, key=lambda x: float(x['growth'].replace('%', '').replace(',', '')), reverse=True)[:10]

        # Save the top 10 companies to JSON files
        with open('top_10_price.json', 'w') as f:
            json.dump(top_10_price, f, indent=4)

        with open('top_10_pe.json', 'w') as f:
            json.dump(top_10_pe, f, indent=4)

        with open('top_10_growth.json', 'w') as f:
            json.dump(top_10_growth, f, indent=4)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
