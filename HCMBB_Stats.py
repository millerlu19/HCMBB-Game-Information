# HCMBB_Stats.py

import requests
from bs4 import BeautifulSoup
import HanoverGame.py

PageUrls = open('PageUrl.txt', 'r')

# helper function to read all of the urls from PageUrl.txt
def get_game_urls():
    return PageUrls

# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page(url):
    return None

def main():
    game_urls = get_game_urls()
    game_pages = []
    for url in game_urls:
        game_pages.append(HanoverGame(get_game_page(url)))

main()