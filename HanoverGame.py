# HanoverGame.py

from bs4 import BeautifulSoup

class HanoverGame:

    def __init__(self, page):
        self.page = page
        self.location = setLocation()
        self.opponent = setOpponent()
        self.HanoverScore = setHanoverScore()
        self.OpponentScore = setOpponentScore()
        self.date = setDate()

    def setLocation(self):
        # get location info from self.page
        return None

    def setOpponent(self):
        soup = BeautifulSoup(self.page.text, 'html.parser')
        Opponent_Name = list(soup.find(class_='head').children)[1].prettify()
        Opponent_Name = Opponent_Name.split()
        if Opponent_Name[1] == "Hanover":
            if len(Opponent_Name[3]) < 4:
                Opponent_Name_List = Opponent_Name[3:6]
                Opponent_Name_String = " ".join(Opponent_Name_List)
                return Opponent_Name_String
            elif len(Opponent_Name[3]) == 4:
                Opponent_Name_List = Opponent_Name[3:5]
                Opponent_Name_String = " ".join(Opponent_Name_List)
                return Opponent_Name_String
            else:
                Opponent_Name_List = Opponent_Name[3]
                Opponent_Name_String = " ".join(Opponent_Name_List)
                return Opponent_Name_String
        else:
            if len(Opponent_Name[1]) <= 4:
                Opponent_Name_List = Opponent_Name[1:4]
                Opponent_Name_String = " ".join(Opponent_Name_List)
                return Opponent_Name_String
            elif len(Opponent_Name[3]) == 4:
                Opponent_Name_List = Opponent_Name[1:3]
                Opponent_Name_String = " ".join(Opponent_Name_List)
                return Opponent_Name_String
            else:
                Opponent_Name_List = Opponent_Name[1]
                Opponent_Name_String = " ".join(Opponent_Name_List)
                return Opponent_Name_String

    def setHanoverScore(self):
        soup = BeautifulSoup(self.page.text, 'html.parser')
        if self.location == "Home":
            HanoverHomeScore = soup.find(class_='team-score home')
            HanoverHomeTotal = list(HanoverHomeScore.children)[0]
            return HanoverHomeTotal
        else:
            HanoverAwayScore = soup.find(class_='team-score visitor')
            HanoverAwayTotal = list(HanoverAwayScore.children)[0]
            return HanoverAwayTotal

    def setOpponentScore(self):
        soup = BeautifulSoup(self.page.text, 'html.parser')
        if self.location == "Home":
            OpponentHomeScore = soup.find(class_='team-score home')
            OpponentHomeTotal = list(OpponentHomeScore.children)[0]
            return OpponentHomeTotal
        else:
            OpponentAwayScore = soup.find(class_='team-score visitor')
            OpponentAwayTotal = list(OpponentAwayScore.children)[0]
            return OpponentAwayTotal

    def setDate(self):
        date = list(soup.find(class_='head').children)[1].prettify()
        game_date_list = date.split()[5:8]
        game_date_string = " ".join(game_date_list)
        return game_date_string

    def getLocation(self):
        return self.location

    def getOpponent(self):
        return self.opponent

    def getHanoverScore(self):
        return self.HanoverScore

    def getOpponentScore(self):
        return self.OpponentScore

    def getDate(self):
        return self.date