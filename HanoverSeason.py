# HanoverSeason.py

import HCMBB_Stats
import HanoverGame

class HanoverSeason(HCMBB_Stats, HanoverGame):

    def __init__(self):
        self.seasons_dict = HCMBB_Stats.get_game_url_dict()
        self.season = self.set_season()
        self.games_dict = self.set_games_dict()
        self.start_date = self.set_start_date()
        self.end_date = self.set_end_date()

    def set_season(self):
        seasons = list(self.seasons_dict.keys())
        season = self.season_from_user(seasons)
        return season

    def season_from_user(self, seasons):
        season_input = int(input("Which Hanover Men's Basketball season would you like to view? Seasons include: {}. ".format(seasons)))
        return season_input

    def full_season_string(self):
        season = self.set_season()
        full_season_str = str(season - 1) + "-" + str(season)
        return full_season_str

    def set_games_dict(self):
        season = self.set_season()
        games = self.seasons_dict[season]
        return games

    def get_games_list(self):
        games_dict = self.set_games_dict()
        games_list = list(games_dict.keys())
        return games_list

    def set_start_date(self):

    def set_end_date(self):

    def get_season(self):
        return self.season

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_games_dict(self):
        return self.games_dict
