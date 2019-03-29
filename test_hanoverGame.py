from unittest import TestCase


class TestHanoverGame(TestCase):
    def test___init__(self):
        import HanoverGame

        # Test 1: Wheaton; 3/1/19
        wheaton_url = "https://hanover.prestosports.com/sports/mbkb/2018-19/boxscores/20190301_0i35.xml"
        vs_wheaton = HanoverGame.HanoverGame(wheaton_url)
        print(vs_wheaton)
        self.assertEqual("Timken Gymnasium; Wooster, Ohio", vs_wheaton.location)
        self.assertEqual("March 1, 2019", vs_wheaton.date)
        self.assertEqual("Wheaton", vs_wheaton.opponent)
        self.assertEqual("73", vs_wheaton.hanover_score)
        self.assertEqual("84", vs_wheaton.opponent_score)

        # Test 2: Butler; 10/28/2017
        butler_url = "https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171028_m0c1.xml"
        vs_butler = HanoverGame.HanoverGame(butler_url)
        print(vs_butler)
        self.assertEqual("Indianapolis, Ind. -- Hinkle Fieldhouse", vs_butler.location)
        self.assertEqual("October 28, 2017", vs_butler.date)
