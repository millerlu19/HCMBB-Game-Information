# HCMBB_Stats.py
from typing import Dict, Any

import requests
from bs4 import BeautifulSoup


# import HanoverGame.py

# def get_urls_dict()
# key = (opponent, date)
# value = url
def get_game_url_dict():
    """
    Returns a list of all the urls of each Hanover games' box scores.
    Two separate Dictionaries for the 2017-2018 season and the 2018-2019 season.
    """
    PageUrls = open('PageUrl.txt', 'r')

    Game_Urls_2018 = {}
    Game_Urls_2019 = {}

    for line in PageUrls:
        line = line.strip()
        if not line.startswith('#') and not len(line) == 0:
            opp, link = line.split(' = ')
            date = link.split('/')[-1].split('_')[0]
            opponent = (opp, date)
            date_int = int(date)
            if date_int <= 20180302:
                Game_Urls_2018[opponent] = link
            else:
                Game_Urls_2019[opponent] = link

    PageUrls.close()

    return Game_Urls_2018, Game_Urls_2019


# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page(game_urls_2019, game_urls_2018):
    """Returns the specific game url for the game that is being selected."""

    filtered_dict = {}
    szn_input = input("Which Hanover Men's Basketball season would you like to view? (2019 or 2018) ")
    if szn_input == "2019":
        opp_input = input("Which game in this season would you like to view? (enter opponent) ")
        for key, val in game_urls_2019.items():
            if opp_input == key[0]:
                filtered_dict[key] = val
        if len(filtered_dict) == 0:
            print("Hanover did not play this team in this season. Please try again.")
            get_game_page(game_urls_2019, game_urls_2018)
        elif len(filtered_dict) == 1:
            return filtered_dict
        else:
            return filtered_dict
    elif szn_input == "2018":
        opp_input = input("Which game in this season would you like to view? (enter opponent) ")
        for key, val in game_urls_2018.items():
            if opp_input == key[0]:
                filtered_dict[key] = val
        if len(filtered_dict) == 0:
            print("Hanover did not play this team in this season. Please try again.")
            get_game_page(game_urls_2019, game_urls_2018)
        elif len(filtered_dict) == 1:
            return filtered_dict
        else:
            return filtered_dict
    else:
        print("This season is not available in this application. Try Either '2019' or '2018.")
        get_game_page(game_urls_2019, game_urls_2018)


def create_game_objects():
    """Returns the info collected from the HanoverGame class for the selected game."""

    return


# main()
# Creates a long list of the box score urls for each game played
# Create a HanoverGame object for each game page url
# dictionary -> key: tuple (opponent, month & day, year), value: HanoverGame object
def main():
    game_urls_2018 = get_game_url_dict()[0]
    print(game_urls_2018)
    game_urls_2019 = get_game_url_dict()[1]
    print(game_urls_2019)

    game_page = get_game_page(game_urls_2018, game_urls_2019)
    print(game_page)


main()
