# HanoverSeason.py

import HCMBB_Stats
import HanoverGame


class HanoverSeason(HCMBB_Stats, HanoverGame):

    def __init__(self, year):
        self.seasons_dict = HCMBB_Stats.get_game_url_dict()
        self.season = self.full_season_string(year)
        self.games_in_season = self.get_opponents_list()
        self.start_date = self.set_start_date()
        self.end_date = self.set_end_date()

    def __str__(self):
        return self.season + " | " + self.start_date + "-" + self.end_date + " | " + self.games_in_season

    # def set_season(self):
    #     seasons = list(self.seasons_dict.keys())
    #     season = self.season_from_user(seasons)
    #     return season

    # def season_from_user(self, seasons):
    #     season_input = int(input("Which Hanover Men's Basketball season would you like to view? Seasons include: {}. ".format(seasons)))
    #     return season_input

    def full_season_string(self, year):
        # season = self.set_season()
        full_season_str = str(year - 1) + "-" + str(year)
        return full_season_str

    def set_games_dict(self):
        season = self.set_season()
        games = self.seasons_dict[season]
        return games

    def get_opponents_list(self):
        games_dict = self.set_games_dict()
        games_list = list(games_dict.keys()[0])
        opp_list = HCMBB_Stats.get_opponent_list(games_list)
        return opp_list

    def set_start_date(self):
        first_game_url = self.set_games_dict()[0]
        return first_game_url.HanoverGame.set_date()

    def set_end_date(self):
        last_game_url = self.set_games_dict()[-1]
        return last_game_url.HanoverGame.set_date()

    def get_season(self):
        return self.season

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_games_dict(self):
        return self.games_dict
