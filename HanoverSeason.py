# HanoverSeason.py

import HCMBB_Stats
import HanoverGame


class HanoverSeason:

    SEASON_START = "10/1/"
    SEASON_END = "3/31/"

    def __init__(self, year, seasons_dict):

        self.season_id = self.set_season_id(year)
        self.games_dict = self.scrape_season_info(seasons_dict[year])
        self.opponents_list = self.get_opponents_list()
        self.start_date = self.set_start_date(year)
        self.end_date = self.set_end_date(year)

        # for game_key in self.games_dict:
        #     print(self.games_dict[game_key])

    def __str__(self):
        return self.season_id + " | " + self.start_date + "-" + self.end_date + " | " + str(self.opponents_list)

    def set_season_id(self, year):
        full_season_str = str(year - 1) + "-" + str(year)
        return full_season_str

    def scrape_season_info(self, season_dict):
        games_dict = {}
        for game_key in season_dict:
            game_url = season_dict[game_key]
            games_dict[game_key] = HanoverGame.HanoverGame(game_url)
        return games_dict

    def get_opponents_list(self):
        return HCMBB_Stats.get_opponent_list(self.games_dict.keys())

    def set_start_date(self, year):
        return HanoverSeason.SEASON_START + str(year-1)

    def set_end_date(self, year):
        return HanoverSeason.SEASON_END + str(year)
