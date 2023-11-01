import requests
from bs4 import BeautifulSoup

# Define the URL for CBS Football Stats
url = "https://www.cbssports.com/nfl/stats/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the dropdown menu
    dropdown = soup.find('select', {'id': 'seasonsDropdown'})

    # Check if the dropdown element is found
    if dropdown:
        # Select the "regular" option if it exists
        regular_option = dropdown.find('option', {'value': '2'})
        if regular_option:
            regular_option['selected'] = 'selected'

            # Find the table containing the top 20 touchdown leaders
            touchdown_table = soup.find('table', {'id': 'player-stats'})

            # Extract and print the data for the top 20 touchdown leaders
            rows = touchdown_table.find_all('tr')[1:21]  # Skip the header row
            for row in rows:
                columns = row.find_all('td')
                player = columns[0].text.strip()
                position = columns[1].text.strip()
                team = columns[2].text.strip()
                touchdowns = columns[3].text.strip()
                print(f"Player: {player}, Position: {position}, Team: {team}, Touchdowns: {touchdowns}")
        else:
            print("Regular option not found in the dropdown.")
    else:
        print("Dropdown menu not found on the page.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
