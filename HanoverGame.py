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
        return None

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
        return None

    def getLocation(self):
        return None

    def getOpponent(self):
        return self.opponent

    def getHanoverScore(self):
        return self.HanoverScore

    def getOpponentScore(self):
        return self.OpponentScore

    def getDate(self):
        return self.date