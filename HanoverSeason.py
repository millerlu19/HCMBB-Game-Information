# HanoverSeason.py

import HCMBB_Stats


class HanoverSeason:

    SEASON_START = "10/1/"
    SEASON_END = "3/31/"

    def __init__(self, year, seasons_dict):
        self.season_id = self.set_season_id(year)
        self.games_dict = seasons_dict[year]
        self.opponents_list = self.get_opponents_list()
        self.start_date = self.set_start_date(year)
        self.end_date = self.set_end_date(year)

    def __str__(self):
        return self.season_id + " | " + self.start_date + "-" + self.end_date + " | " + str(self.opponents_list)

    def set_season_id(self, year):
        full_season_str = str(year - 1) + "-" + str(year)
        return full_season_str

    def get_opponents_list(self):
        return HCMBB_Stats.get_opponent_list(self.games_dict.keys())

    def set_start_date(self, year):
        return HanoverSeason.SEASON_START + str(year-1)

    def set_end_date(self, year):
        return HanoverSeason.SEASON_END + str(year)

    def get_season_id(self):
        return self.season_id

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_games_dict(self):
        return self.games_dict
