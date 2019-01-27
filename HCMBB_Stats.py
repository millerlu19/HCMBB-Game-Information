# HCMBB_Stats.py

import requests
from bs4 import BeautifulSoup
import HanoverGame.py

# helper function to read all of the urls from PageUrl.txt
def get_game_urls():
    PageUrls = open('PageUrl.txt', 'r')
    game_pages = []
    for url in game_urls:
        game_pages.append(HanoverGame(get_game_page(url)))
    return game_pages

# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page(url):
    return game_pages[url]

# main()
# Creates a long list of the box score urls for each game played
# Create a HanoverGame object for each game page url
    # dictionary -> key: tuple (opponent, month & day, year), value: HanoverGame object
def main():
    game_urls = get_game_urls()
    print(game_urls)

main()