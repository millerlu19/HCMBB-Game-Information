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
        return None

    def setOpponentScore(self):
        return None

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