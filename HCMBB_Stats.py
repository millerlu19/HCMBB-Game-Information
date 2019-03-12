# HCMBB_Stats.py
from typing import Dict, Any

import requests
from bs4 import BeautifulSoup


# import HanoverGame.py

START_YEAR = 2018

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

    #Game_Urls = {}
    #YearList = gen_year_list(START_YEAR)
    #for year in YearList:
    #   Game_Urls[year] = {}

    for line in PageUrls:
        line = line.strip()
        if is_game_line(line):
            opp, link = line.split(' = ')
            date = get_date(link)
            game_key = (opp, date)
            season = get_season(date)
            Game_Urls[season][game_key] = link

    PageUrls.close()

    return Games_Urls

def is_game_line(line):
    return not line.startswith('#') and not len(line) == 0

def get_date(link):
    date = link.split('/')[-1].split('_')[0]
    return int(date)

def get_season(date):


def gen_year_list(start_year):


# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page(game_urls_2018, game_urls_2019):
    """Returns the specific game url for the game that is being selected."""

    szn_input = input("Which Hanover Men's Basketball season would you like to view? (2019 or 2018) ")
    while szn_input != "2018" and szn_input != "2019":
        szn_input = input("This season is not available in this application. Try Either '2019' or '2018'. ")
    filtered_dict = {}
    if szn_input == "2018":
        opp_input = input("Which game in this season would you like to view? (enter opponent) ")
        # Attempting to use valid_game() function
        valid = valid_game(opp_input, game_urls_2018)
        for key, val in game_urls_2018.items():
            if valid == key[0]:
                filtered_dict[key] = val
        # Need to figure out how to keep looping the opp_input variable if input is not valid
        # try helper function valid_game() ???
        if len(filtered_dict) == 0:
            print("Hanover did not play this team in this season. Please try again: ")
        elif len(filtered_dict) == 1:
            for opp in filtered_dict:
                return filtered_dict[opp]
        else:
            for key, val in filtered_dict.items():
                print(key[1])
            date_input = input("Hanover has played this team multiple times. Enter date of game you want to see: ")
            for key, val in filtered_dict.items():
                if date_input == key[1]:
                    return val
    elif szn_input == "2019":
        opp_input = input("Which game in this season would you like to view? (enter opponent) ")
        # Attempting to use valid_game() function
        valid = valid_game(opp_input, game_urls_2019)
        for key, val in game_urls_2019.items():
            if valid == key[0]:
                filtered_dict[key] = val
        # Need to figure out how to keep looping the opp_input variable if input is not valid
        print(filtered_dict)
        if len(filtered_dict) == 1:
            for opp in filtered_dict:
                return filtered_dict[opp]
        else:
            for key, val in filtered_dict.items():
                print(key[1])
            date_input = input("Hanover has played this team multiple times. Enter date of game you want to see: ")
            for key, val in filtered_dict.items():
                if date_input == key[1]:
                    return val

def valid_game(opp, game_dict):
    # Almost have this completely working
    # messes up if there are a few invalid opponent inputs followed by a valid input
    # print(opp) stops at selected opponent but says "Please try again:" and ends program
    """Returns the opponent's name as a string if valid in the season's dictionary."""

    print(game_dict)
    print(opp)
    for key, val in game_dict.items():
        print(key[0])
        if opp == key[0]:
            return opp
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
