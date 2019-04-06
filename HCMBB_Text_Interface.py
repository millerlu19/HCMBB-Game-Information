# HCMBB_Text_Interface.py

import HCMBB_Stats
import HanoverSeason


def main():
    seasons_dict = HCMBB_Stats.get_game_url_dict()
    seasons_list = list(seasons_dict.keys())
    print("Scraping data. This will take awhile...\n")
    seasons_data = {}
    for year in seasons_list:
        season = HanoverSeason.HanoverSeason(year, seasons_dict)
        seasons_data[season.season_id] = season
    print("Thanks for waiting! Starting demo...\n")

    for season_id in seasons_data.keys():
        print(season_id)
    print("\n")
    season_input = input("Select Season: ")

    season_inp_data = seasons_data[season_input]
    game_number = 1
    for game_key in season_inp_data.games_dict:
        game = season_inp_data.games_dict[game_key]
        print(game_number, "->", game.date + ":", game.opponent + ",", game.result)
        game_number += 1
    print("\n")
    game_input = int(input("Select game number: "))

    opp_list = seasons_data[season_input].opponents_list
    opp_name = opp_list[game_input-1]
    print("\n")

    game_keys = seasons_data[season_input].games_dict.keys()
    for key in game_keys:
        if key[0] == opp_name:
            game_key = key
            break
    sel_game = season_inp_data.games_dict[game_key]

    print("Date:", sel_game.date, "\n")
    print(sel_game.result + ",", "Hanover:", sel_game.hanover_score, sel_game.opponent + ":", sel_game.opponent_score,
          "\n")
    print("Game Location:", sel_game.location)
    print("\n")
    view_game = input("Would you like to view another game (y or n)? ")
    while view_game == "y":
        main()


main()
