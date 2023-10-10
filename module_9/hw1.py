import requests
from bs4 import BeautifulSoup
import json

# Step 1: Make an HTTP request to the S&P500 index page
url = "https://markets.businessinsider.com/index/components/s&p_500"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 2: Parse the list of company links
    company_links = [a["href"] for a in soup.select(".table__tbody td:nth-child(1) a")]

    # Initialize lists to store company data
    companies = []

    # Iterate through each company link
    for company_link in company_links[:10]:  # Limit to the top 10 companies for now
        # Step 3: Visit the company's page and extract required information
        company_url = f"https://markets.businessinsider.com{company_link}"
        company_response = requests.get(company_url)

        if company_response.status_code == 200:
            company_soup = BeautifulSoup(company_response.text, "html.parser")

            # Extract price, code, name, and growth
            price = company_soup.select_one(".price-section__current-value").text
            code = company_soup.select_one(".price-section__label").text
            name = company_soup.select_one(".price-section__identifiers .price-section__label").text

            # Find the P/E ratio using a CSS selector
            pe_label = company_soup.select_one(".key-data-currency")
            pe_ratio = pe_label.find_next("span").text if pe_label else "N/A"

            # Find the growth data using the previous locator
            growth_data = company_soup.select_one(".historical-prices__price-change-values span:first-of-type").text

            # Step 4: Store information for each company in a dictionary
            company_data = {
                "code": code,
                "name": name,
                "price": price,
                "P/E": pe_ratio,
                "growth": growth_data,
            }
            companies.append(company_data)

    # Step 5: Save the top 10 companies in a JSON file
    with open("top_10_companies.json", "w") as json_file:
        json.dump(companies, json_file, indent=4)

    expensive_file = 'top_10_expensive.json'
    lowest_pe_file = 'top_10_lowest_pe.json'
    most_growth_file = 'top_10_most_growth.json'


    # Define a function to save data to JSON
    def save_to_json(data, file_path):
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)


    # Sort and save the top 10 companies with the most expensive shares
    top_10_expensive = sorted(companies, key=lambda x: x['price'], reverse=True)[:10]
    save_to_json(top_10_expensive, expensive_file)

    # Sort and save the top 10 companies with the lowest P/E
    top_10_lowest_pe = sorted(companies, key=lambda x: x['P/E'])[:10]
    save_to_json(top_10_lowest_pe, lowest_pe_file)

    # Sort and save the top 10 companies with the most growth for the last year
    top_10_most_growth = sorted(companies, key=lambda x: x['growth'], reverse=True)[:10]
    save_to_json(top_10_most_growth, most_growth_file)

    print("Top 10 companies data saved in 'top_10_companies.json' file.")
