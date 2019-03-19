# HCMBB_Stats.py
from typing import Dict, Any

import requests
from bs4 import BeautifulSoup


# import HanoverGame.py
# import HanoverSeason.py
import datetime

today = datetime.datetime.today()
current_year = today.year


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

    game_urls = {}
    season_list = gen_season_list(START_YEAR)
    for season in season_list:
        game_urls[season] = {}

    for line in PageUrls:
        line = line.strip()
        if is_game_line(line):
            opp, link = line.split(' = ')
            date = get_date(link)
            game_key = (opp, date)
            season = get_season(date)
            game_urls[season][game_key] = link

    PageUrls.close()

    return game_urls

def gen_season_list(start_year):
    """
    Returns a list of the number of seasons this program has games for.
    Exa: [2018, 2019].
    """
    years = []
    for year in range(start_year, current_year + 1):
        years.append(year)
    return years

def is_game_line(line):
    """
    Returns true if the line in the PageUrl text file is a box score link.
    Returns false if the line is blank or a comment.
    """
    return not line.startswith('#') and not len(line) == 0

def get_date(link):
    """
    Returns the date of the game played in the form it is shown in the box score link.
    Turns date into an integer.
    """
    date = link.split('/')[-1].split('_')[0]
    return int(date)

def get_season(date):
    """
    Returns the season that the specific basketball game was played in.
    2018 -> 2017-2018 season.
    2019 -> 2018-2019 season.
    """
    year = date // 10000
    breakpoint = (year * 10000) + 700
    if date < breakpoint:
        return year
    else:
        return year + 1

# helper function that takes the url and opens the page through a get request and returns the page
def get_game_page(seasons_dict, season, game_key):
    """Returns the specific game url for the game that is being selected."""

# Why does this not work?
    return seasons_dict[season][game_key]

    # filtered_dict = {}
    # if season == "2018":
    #     opp_input = input("Which game in this season would you like to view? (enter opponent) ")
    #     # Attempting to use valid_game() function
    #     valid = valid_game(opp_input, season_dict)
    #     for key, val in game_urls_2018.items():
    #         if valid == key[0]:
    #             filtered_dict[key] = val
    #     # Need to figure out how to keep looping the opp_input variable if input is not valid
    #     # try helper function valid_game() ???
    #     if len(filtered_dict) == 0:
    #         print("Hanover did not play this team in this season. Please try again: ")
    #     elif len(filtered_dict) == 1:
    #         for opp in filtered_dict:
    #             return filtered_dict[opp]
    #     else:
    #         for key, val in filtered_dict.items():
    #             print(key[1])
    #         date_input = input("Hanover has played this team multiple times. Enter date of game you want to see: ")
    #         for key, val in filtered_dict.items():
    #             if date_input == key[1]:
    #                 return val
    # elif szn_input == "2019":
    #     opp_input = input("Which game in this season would you like to view? (enter opponent) ")
    #     # Attempting to use valid_game() function
    #     valid = valid_game(opp_input, game_urls_2019)
    #     for key, val in game_urls_2019.items():
    #         if valid == key[0]:
    #             filtered_dict[key] = val
    #     # Need to figure out how to keep looping the opp_input variable if input is not valid
    #     print(filtered_dict)
    #     if len(filtered_dict) == 1:
    #         for opp in filtered_dict:
    #             return filtered_dict[opp]
    #     else:
    #         for key, val in filtered_dict.items():
    #             print(key[1])
    #         date_input = input("Hanover has played this team multiple times. Enter date of game you want to see: ")
    #         for key, val in filtered_dict.items():
    #             if date_input == key[1]:
    #                 return val

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
    seasons_dict = get_game_url_dict()
    seasons = seasons_dict.keys()
    season_input = int(input("Which Hanover Men's Basketball season would you like to view? Seasons include: {}. ".format(seasons)))
# Would like to set games to equal just the opponent name instead of the tuple with the opponent and date
#   exa: "Spalding" instead of "('Spalding, 20181113)"
    games = seasons_dict[season_input].keys()
    game_input = input("Which game in this Hanover season would you like to view? Games include: {}. ".format(games))
    get_game_page(seasons_dict, season_input, game_input)


main()
