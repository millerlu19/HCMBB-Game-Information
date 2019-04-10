# HCMBB_Text_Interface.py

import HCMBB_Stats
import HanoverSeason

# import http.server
# import socketserver
#
# PORT = 8080
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     httpd.serve_forever()


def scrape_data():
    seasons_dict = get_seasons_dict()
    seasons_list = list(seasons_dict.keys())
    print("Scraping data. This will take awhile...\n")
    seasons_data = {}
    for year in seasons_list:
        season = HanoverSeason.HanoverSeason(year, seasons_dict)
        seasons_data[season.season_id] = season
    print("Thanks for waiting! Starting demo...\n")

    get_game_info(seasons_data)


def get_seasons_dict():
    return HCMBB_Stats.get_game_url_dict()


def select_season(seasons_data):
    for season_id in seasons_data.keys():
        print(season_id)
    print("\n")
    season_input = input("Select Season: ")
    return season_input


def game_keys_in_szn(seasons_dict, year):
    return list(seasons_dict[year].keys())


def get_szn_inp_data(seasons_data, season_input):
    return seasons_data[season_input]


def select_game(season_inp_data):
    print("\n")
    game_number = 1
    for game_key in season_inp_data.games_dict:
        game = season_inp_data.games_dict[game_key]
        print(game_number, "->", game.date + ":", game.opponent + ",", game.result)
        game_number += 1
    print("\n")
    game_input = int(input("Select game number: "))
    return game_input


def get_opponent_name(season_inp_data, game_input):
    opp_list = season_inp_data.opponents_list
    opp_name = opp_list[game_input - 1]
    print("\n")
    return opp_name


def get_game_key(game_keys, game_input):
    return game_keys[game_input-1]


def get_game_inp_data(season_inp_data, game_key):
    return season_inp_data.games_dict[game_key]


def get_game_info(seasons_data):
    seasons_dict = get_seasons_dict()
    season_input = select_season(seasons_data)
    game_keys = game_keys_in_szn(seasons_dict, int(season_input[-4:]))
    # season_input_data -> HanoverSeason
    season_input_data = get_szn_inp_data(seasons_data, season_input)
    game_input = select_game(season_input_data)
    game_key = get_game_key(game_keys, game_input)
    game_input_data = get_game_inp_data(season_input_data, game_key)

    print("Date:", game_input_data.date, "\n")
    print(game_input_data.result + ",", "Hanover:", game_input_data.hanover_score, game_input_data.opponent + ":",
          game_input_data.opponent_score, "\n")
    print("Game Location:", game_input_data.location)
    print("\n")

    view_new_game = input("Would you like to view another game (y or n)? ")
    if view_new_game == "y":
        get_game_info(seasons_data)
    else:
        return


scrape_data()
