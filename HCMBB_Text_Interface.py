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
            result = "W"
        else:
            result = "L"
        print(game_number, "->", game_date + ":", game_opp + ",", result, hanover_score, "-", opp_score)
        game_number += 1


main()
