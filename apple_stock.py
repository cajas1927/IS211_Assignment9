import requests
from bs4 import BeautifulSoup

# Define the URL for Apple stock data on Yahoo Finance
url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing historical stock prices
    table = soup.find('table', {'data-test': 'historical-prices'})

    # Extract and print the date and close price for all dates
    rows = table.find_all('tr')[1:]  # Skip the header row
    for row in rows:
        columns = row.find_all('td')
        date = columns[0].text.strip()
        close_price = columns[4].text.strip()
        print(f"Date: {date}, Close Price: {close_price}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
