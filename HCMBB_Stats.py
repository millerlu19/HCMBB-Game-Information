# HCMBB_Stats.py

import requests
from bs4 import BeautifulSoup
#import HanoverGame.py

# helper function to read all of the urls from PageUrl.txt
def get_game_urls():
    """
    Returns a list of all the urls of each Hanover games' box scores.
    Two separate Lists for the 2017-2018 season and the 2018-2019 season.
    """
    PageUrls = open('PageUrl.txt', 'r')
    Txt_File_List = PageUrls.readlines()
    Urls_List = []
    for url in Txt_File_List:
        url = url.rstrip()
        if not url.startswith('#'):
            Urls_List.append(url)

    Urls_List_18 = Urls_List[:30]
    Urls_List_19 = Urls_List[31:]

    PageUrls.close()

    return Urls_List_18, Urls_List_19

# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page(url):
    """Returns the info of the selected game's box score page from Hanover Presto Sports."""

    return game_pages[url]

# main()
# Creates a long list of the box score urls for each game played
# Create a HanoverGame object for each game page url
    # dictionary -> key: tuple (opponent, month & day, year), value: HanoverGame object
def main():
    Game_URLs_2018 = get_game_urls()[0]
    print(Game_URLs_2018)
    Game_URLs_2019 = get_game_urls()[1]
    print(Game_URLs_2019)

main()