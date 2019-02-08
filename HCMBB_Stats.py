# HCMBB_Stats.py

import requests
from bs4 import BeautifulSoup
#import HanoverGame.py

# helper function to read all of the urls from PageUrl.txt
def get_urls_list():
#MAKE SURE TO FIX UP TEXT FILE BEFORE TESTING THIS FUNCTION AGAIN
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

    Urls_List_18 = Urls_List[:32]
    Urls_List_19 = Urls_List[33:]

    PageUrls.close()

    return Urls_List_18, Urls_List_19

# def get_urls_dict()
# key = (opponent, date)
# value = url
def get_urls_dict():
    """
    Returns a list of all the urls of each Hanover games' box scores.
    Two separate Dictionaries for the 2017-2018 season and the 2018-2019 season.
    """
    PageUrls = open('PageUrl.txt', 'r')

    Urls_Dict = {}
    for line in PageUrls:
        line = line.strip()
        print(line)
        if not line.startswith('#') and not len(line) == 0:
            opp, link = line.split(' = ')
            date = link.split('/')[-1].split('_')[0]
            opponent = (opp, date)
            print(opponent)
            Urls_Dict[opponent] = link
            print(Urls_Dict)
            print(len(Urls_Dict))

    PageUrls.close()

    return Urls_Dict

# helper function that takes in the game url as a parameter and returns the date of the selected game played
def get_game_date(url):
    """Returns the date of the selected game played from its url"""


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
    #Urls_List_2018 = get_urls_list()[0]
    #print(Urls_List_2018)
    #Urls_List_2019 = get_urls_list()[1]
    #print(Urls_List_2019)

    Urls_Dict = get_urls_dict()
    print(Urls_Dict)

main()