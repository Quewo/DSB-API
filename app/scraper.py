import json
from bs4 import BeautifulSoup 
import requests
import os


# load the config.json file and set global variables
def load_config() -> None:
     # Get the directory of the current file (scraper.py)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to config.json
    config_path = os.path.join(dir_path, 'config.json')

    with open(config_path) as config_file:
        global config_data, URL
        config_data = json.load(config_file)
        URL = config_data['url']


def scrape_data(url):
    # Set up headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8',
        'Referer': 'https://www.dsbmobile.de/'
    }
    
    # Send GET request
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract desired data (this is a placeholder - you'd need to specify what data to extract)
        data = soup.find_all('td', class_='list')
        
        return data
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# URL to scrape
url = "https://dsbmobile.de/data/a3dd0624-17cd-492e-bd67-b63d1fa53ef8/05cf4219-b054-41b5-b0b5-b9d8e741d089/05cf4219-b054-41b5-b0b5-b9d8e741d089.htm"

# Scrape data
scraped_data = scrape_data(url)

if scraped_data:
    for data in scraped_data:
        print(data.text)
