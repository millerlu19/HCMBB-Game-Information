# HCMBB_Text_Interface.py

import HCMBB_Stats
import HanoverSeason
import HanoverGame


def main():
    seasons_dict = HCMBB_Stats.get_game_url_dict()
    # seasons_list = [2018, 2019] <- list of ints
    seasons_list = list(seasons_dict.keys())
    for year in seasons_list:
        print(HanoverSeason.HanoverSeason(year, seasons_dict).season_id)
    season_input = input("Select Season: ")

    season_year = int(season_input[-4:])
    # season_inp_dict = dictionary of each game in season {(opponent, date_id): url}
    season_inp_dict = seasons_dict[season_year]
    game_number = 1
    for game in season_inp_dict:
        game_url = season_inp_dict[game]
        game_date = HanoverGame.HanoverGame(game_url).date
        game_opp = HanoverGame.HanoverGame(game_url).opponent
        hanover_score = HanoverGame.HanoverGame(game_url).hanover_score
        opp_score = HanoverGame.HanoverGame(game_url).opponent_score
        if hanover_score > opp_score:
            game_result = "W"
        else:
            game_result = "L"
        print(game_number, "->", game_date + ":", game_opp + ",", game_result, hanover_score, "-", opp_score)
        game_number += 1
    game_input = int(input("Select game number: "))

    opp_list = HanoverSeason.HanoverSeason(season_year, seasons_dict).opponents_list
    opp_name = opp_list[game_input-1]
    game_keys = seasons_dict[season_year].keys()
    for key in game_keys:
        if key[0] == opp_name:
            game_key = key
    sel_game_url = seasons_dict[season_year][game_key]
    sel_game_date = HanoverGame.HanoverGame(sel_game_url).date
    sel_game_opp = HanoverGame.HanoverGame(sel_game_url).opponent
    sel_game_hc_score = HanoverGame.HanoverGame(sel_game_url).hanover_score
    sel_game_opp_score = HanoverGame.HanoverGame(sel_game_url).opponent_score
    sel_game_location = HanoverGame.HanoverGame(sel_game_url).location
    if sel_game_hc_score > sel_game_opp_score:
        sel_game_result = "W"
    else:
        sel_game_result = "L"
    print("Date:", sel_game_date, "\n")
    print(sel_game_result + ",", "Hanover:", sel_game_hc_score, sel_game_opp + ":", sel_game_opp_score, "\n")
    print("Game Location:", sel_game_location)


main()
