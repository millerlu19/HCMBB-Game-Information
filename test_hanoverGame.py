from unittest import TestCase


class TestHanoverGame(TestCase):
    def test___init__(self):
        import HanoverGame
        url = "https://hanover.prestosports.com/sports/mbkb/2018-19/boxscores/20190301_0i35.xml"
        hanover_game = HanoverGame.HanoverGame(url)
        print(hanover_game)
        self.assertEquals("Timken Gymnasium; Wooster, Ohio", hanover_game.location)
        self.assertEquals("Wheaton", hanover_game.opponent)
        self.assertEquals("March 1, 2019", hanover_game.date)
        self.assertEquals("73", hanover_game.HanoverScore)
        self.assertEquals("84", hanover_game.OpponentScore)
