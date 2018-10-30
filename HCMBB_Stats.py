# HCMBB_Stats.py

import requests
from bs4 import BeautifulSoup
import HanoverGame.py

# helper function to read all of the urls from PageUrl.txt
def get_game_urls():
    return None

# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page():
    return None

def main():
    game_urls = get_game_urls()
    game_list = []
    for url in game_urls:
        game_list.append(HanoverGame(get_game_page(url)))

main()