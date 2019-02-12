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
def get_game_page(game_urls_2018, game_urls_2019):
    """Returns the specific game url for the game that is being selected."""

    szn_input = input("Which Hanover Men's Basketball season would you like to view? (2019 or 2018) ")
    while szn_input != "2018" and szn_input != "2019":
        szn_input = input("This season is not available in this application. Try Either '2019' or '2018'. ")
    filtered_dict = {}
    if szn_input == "2018":
        opp_input = input("Which game in this season would you like to view? (enter opponent) ")
        for key, val in game_urls_2018.items():
            if opp_input == key[0]:
                filtered_dict[key] = val
        #Need to figure out how to keep looping the opp_input variable if input is not valid
        #try helper function valid_game() ???
        if len(filtered_dict) == 0:
            print("Hanover did not play this team in this season. Please try again: ")
        elif len(filtered_dict) == 1:
            for opp in filtered_dict:
                return filtered_dict[opp]
        else:
            for k, v in filtered_dict.items():
                print(k[1])
            date_input = input("Hanover has played this team multiple times. Enter date of game you want to see: ")
            for k, v in filtered_dict.items():
                if date_input == k[1]:
                    return v
    elif szn_input == "2019":
        opp_input = input("Which game in this season would you like to view? (enter opponent) ")
        for key, val in game_urls_2019.items():
            if opp_input == key[0]:
                filtered_dict[key] = val
        # Need to figure out how to keep looping the opp_input variable if input is not valid
        # try helper function valid_game() ???
        if len(filtered_dict) == 0:
            print("Hanover did not play this team in this season. Please try again: ")
        elif len(filtered_dict) == 1:
            for opp in filtered_dict:
                return filtered_dict[opp]
        else:
            for k, v in filtered_dict.items():
                print(k[1])
            date_input = input("Hanover has played this team multiple times. Enter date of game you want to see: ")
            for k, v in filtered_dict.items():
                if date_input == k[1]:
                    return v

def valid_game(opp, game_dict):
    for key, val in game_dict:
        if opp == key[0]:
            return True
        else:
            new_opp_input = input("Hanover did not play this team in this season. Please try again: ")
            valid_game(new_opp_input, game_dict)

def create_game_objects():
    """Returns the info collected from the HanoverGame class for the selected game."""


    return

def main():
#Store the dictionaries for each HCMBB season under variables by calling the get_game_url_dict() function
    #key=(opponent, date), value=url
    game_urls_2018 = get_game_url_dict()[0]
    game_urls_2019 = get_game_url_dict()[1]

#Store the specific game url that the user selects by calling the get_game_page() function
    game_page = get_game_page(game_urls_2018, game_urls_2019)
    print(game_page)


main()
