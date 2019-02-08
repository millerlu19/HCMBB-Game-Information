# HCMBB_Stats.py

import requests
from bs4 import BeautifulSoup
#import HanoverGame.py

# def get_urls_dict()
# key = (opponent, date)
# value = url
def get_game_url_dict():
    """
    Returns a list of all the urls of each Hanover games' box scores.
    Two separate Dictionaries for the 2017-2018 season and the 2018-2019 season.
    """
    PageUrls = open('PageUrl.txt', 'r')

    Game_Url_Dict = {}
    Game_Urls_2018 = {}
    Game_Urls_2019 = {}
    for line in PageUrls:
        line = line.strip()
        if not line.startswith('#') and not len(line) == 0:
            opp, link = line.split(' = ')
            date = link.split('/')[-1].split('_')[0]
            opponent = (opp, date)
            Game_Url_Dict[opponent] = link

    #Game_Urls_2018 = Game_Url_Dict[:31]
    #Game_Urls_2019 = Game_Url_Dict[31:]

    PageUrls.close()

    return Game_Url_Dict
    #return Game_Urls_2018, Game_Urls_2019

# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page():
    """Returns the specific game url for the game that is being selected."""

    return

def create_game_objects():
    """Returns the info collected from the HanoverGame class for the selected game."""

    return

# main()
# Creates a long list of the box score urls for each game played
# Create a HanoverGame object for each game page url
    # dictionary -> key: tuple (opponent, month & day, year), value: HanoverGame object
def main():
    Game_Url_Dict = get_game_url_dict()
    print(Game_Url_Dict)

main()