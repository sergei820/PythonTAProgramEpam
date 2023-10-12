import requests
from bs4 import BeautifulSoup
import json


url = "https://markets.businessinsider.com/index/components/s&p_500"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    company_links = [a["href"] for a in soup.select(".table__tbody td:nth-child(1) a")]
    companies = []

    for company_link in company_links:
        company_url = f"https://markets.businessinsider.com{company_link}"
        company_response = requests.get(company_url)

        if company_response.status_code == 200:
            company_soup = BeautifulSoup(company_response.text, "html.parser")

            price = company_soup.select_one(".price-section__current-value").text
            code = company_soup.select_one(".price-section__category span").text.replace(", ", "")
            name = company_soup.select_one(".price-section__identifiers .price-section__label").text
            pe_label = company_soup.select_one("#snapshot-highlow + div + div + div")
            pe_ratio = pe_label.find_next("span").text if pe_label else "N/A"
            growth_data = company_soup.select_one(".historical-prices__price-change-values span:first-of-type").text

            company_data = {
                "code": code,
                "name": name,
                "price": price,
                "P/E": pe_ratio,
                "growth": growth_data,
            }
            companies.append(company_data)

    def save_to_json(data, file_path):
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    top_10_expensive = sorted(companies, key=lambda x: x['price'], reverse=True)[:10]
    save_to_json(top_10_expensive, 'top_10_expensive.json')

    top_10_lowest_pe = sorted(companies, key=lambda x: x['P/E'])[:10]
    save_to_json(top_10_lowest_pe, 'top_10_lowest_pe.json')

    top_10_most_growth = sorted(companies, key=lambda x: x['growth'], reverse=True)[:10]
    save_to_json(top_10_most_growth, 'top_10_most_growth.json')
