import json
import bs4
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


# Read the URL from config.json
def scrape():
    load_config()

    req = requests.get(URL)
    if req.status_code == 200:
        soup = bs4.BeautifulSoup(req.text, 'html.parser')

    return soup