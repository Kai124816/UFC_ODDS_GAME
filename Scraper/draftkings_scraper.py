import requests
from bs4 import BeautifulSoup

# URL of the DraftKings UFC Fight Lines page
url = 'https://sportsbook.draftkings.com/leagues/mma/ufc?category=fight-lines&subcategory=fight-lines'

# Send a GET request to fetch the page
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

def get_moneylines(card_length:int)->list[list[list]]:
# Check if the request was successful
    if response.status_code == 200:
        print("Page successfully fetched.")
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the fight rows (specific to the DraftKings layout)
    odds_elements = soup.find_all('span', class_='sportsbook-odds american no-margin default-color')

    odds = [element.text.strip() for element in odds_elements[:card_length*2]]

    fighter_elements = soup.find_all('div', class_="event-cell__name-text")

    fighters = [element.text.strip() for element in fighter_elements[:card_length*2]]

    odds_list = []
    for i in range(card_length*2):
        pair1 = []
        fighter1 = fighters[i-1]
        pair1.append(fighter1)
        odds1 = odds[i-1]
        pair1.append(odds1)
        pair2 = []
        fighter2 = fighters[i]
        pair2.append(fighter2)
        odds2 = odds[i]
        pair2.append(odds2)
        final_pair = []
        final_pair.append(pair1)
        final_pair.append(pair2)
        odds_list.append(final_pair)
    return odds_list





        

        



