# HCMBB_Stats.py

import datetime

today = datetime.datetime.today()
current_year = today.year


START_YEAR = 2018


def get_game_url_dict():
    """
    Returns a list of all the urls of each Hanover games' box scores.
    Two separate Dictionaries for the 2017-2018 season and the 2018-2019 season.
    """
    page_urls = open('PageUrl.txt', 'r')

    game_urls = {}
    season_list = gen_season_list(START_YEAR)
    for season in season_list:
        game_urls[season] = {}

    for line in page_urls:
        line = line.strip()
        if is_game_line(line):
            opp, link = line.split(' = ')
            date = get_date(link)
            game_key = (opp, date)
            season = get_season(date)
            game_urls[season][game_key] = link

    page_urls.close()

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


def get_opponent_list(game_keys):
    """Returns a list of only the opponent names from a specific season."""

    return [game[0] for game in game_keys]


def get_game_key(game_keys, opp_list, opp):
    """Returns the specific game_key tuple based off of the user's game_input entry in the main function."""

    game_key_list = []

    for i in range(len(opp_list)):
        if opp_list[i] == opp:
            game_key_list.append(game_keys[i])

    dates = [game[1] for game in game_key_list]

    if len(game_key_list) == 1:
        return game_key_list[0]
    else:
        game_date = int(input("Hanover has played this team multiple times. What is the date of the specific game you "
                               "would like to see? Dates include: {}. ".format(dates)))
        for i in range(len(dates)):
            if dates[i] == game_date:
                return game_key_list[i]


def get_game_page(seasons_dict, season, game_key):
    """Returns the specific game url for the game that is being selected."""

    return seasons_dict[season].get(game_key)


# def create_game_objects():
#     """Returns the info collected from the HanoverGame class for the selected game."""
#
#
#     return None


def main():
    seasons_dict = get_game_url_dict()
    # print(seasons_dict)
    # seasons = list(seasons_dict.keys())
    # season_input = int(input("Which Hanover Men's Basketball season would you like to view? Seasons include: {}. ".format(seasons)))
    # season = seasons_dict[season_input]
    # game_list = list(season.keys())
    # print(game_list)
    # games = get_opponent_list(game_list)
    # print(games)
    # game_input = input("Which game in this Hanover season would you like to view? Games include: {}. ".format(games))
    # game_key = get_game_key(game_list, games, game_input)
    # print(game_key)
    # game_page = get_game_page(seasons_dict, season_input, game_key)
    # print(game_page)
    # hanover_game = HanoverGame.HanoverGame(game_page)
    # print(hanover_game)


main()
