import json
import bs4
import requests

# Read the URL from config.json
def scrape():
    with open('config.json') as config_file:
        global config_data
        config_data = json.load(config_file)
        URL = config_data['url']

    req = requests.get(URL)
    if req.status_code == 200:
        soup = bs4.BeautifulSoup(req.text, 'html.parser')

    return soup