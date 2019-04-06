# HanoverGame.py

from bs4 import BeautifulSoup
import requests
import re


class HanoverGame:

    def __init__(self, page_url):
        req = requests.get(page_url)
        self.page = BeautifulSoup(req.content, 'html.parser')
        self.location = self.set_location()
        self.opponent = self.set_opponent()
        self.hanover_score = self.set_hanover_score()
        self.opponent_score = self.set_opponent_score()
        self.date = self.set_date()
        self.result = self.set_result()

    def __str__(self):
        return self.location + " | " + "Hanover: " + self.hanover_score + " | " + self.opponent + ": " \
               + self.opponent_score + " | " + self.date

    def set_location(self):
        game_info = self.page.find(class_='game-info')
        game_info_2 = list(game_info.children)[1].prettify()
        location_split = re.split('Location:\n    </th>\n    <td class="text">\n     ', game_info_2)
        location = re.split("\n", location_split[1])
        return location[0]

    def set_opponent(self):
        opponent_name = list(self.page.find(class_='head').children)[1].prettify()
        opponent_name = opponent_name.split()
        if opponent_name[1] == "Hanover":
            return self.find_opponent_name(opponent_name, 3)
        else:
            return self.find_opponent_name(opponent_name, 1)

    def find_opponent_name(self, opponent_name, index):
        if len(opponent_name[index]) < 4 or opponent_name[index] == "Kent":
            if opponent_name[index+2] == "-":
                opponent_name_list = opponent_name[index:index+4]
                return self.opponent_to_string(opponent_name_list)
            else:
                opponent_name_list = opponent_name[index:index+3]
                return self.opponent_to_string(opponent_name_list)
        elif len(opponent_name[index]) == 4:
            opponent_name_list = opponent_name[index:index+2]
            return self.opponent_to_string(opponent_name_list)
        else:
            opponent_name_string = opponent_name[index]
            return opponent_name_string

    def opponent_to_string(self, opponent_name):
        opponent_name_string = " ".join(opponent_name)
        return opponent_name_string

    def set_hanover_score(self):
        if self.is_home_game():
            return self.set_home_score()
        else:
            return self.set_away_score()

    def set_opponent_score(self):
        if self.is_home_game():
            return self.set_away_score()
        else:
            return self.set_home_score()

    def is_home_game(self):
        if self.location[:7] == "Collier" or self.location[:7] == "Hanover":
            return True
        elif self.get_home_team_from_header() == "Hanover":
            return True
        else:
            return False

    def set_home_score(self):
        home_score = self.page.find(class_='team-score home')
        home_total = int(list(home_score.children)[0])
        return home_total

    def set_away_score(self):
        away_score = self.page.find(class_='team-score visitor')
        away_total = int(list(away_score.children)[0])
        return away_total

    def set_date(self):
        date = list(self.page.find(class_='head').children)[1].prettify()
        date_split = re.split("<span>\n  ", date)
        game_date = re.split("\n", date_split[-1])
        return game_date[0]

    def set_result(self):
        if self.hanover_score > self.opponent_score:
            return "W"
        else:
            return "L"

    def get_home_team_from_header(self):
        game_header = self.page.find(class_='head')
        game_title = list(game_header.children)[1].prettify()
        game_title = re.split('\n', game_title)
        game_title = game_title[1]
        home_team = game_title[-7:]
        return home_team
