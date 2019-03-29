from unittest import TestCase


class TestHanoverGame(TestCase):
    def test___init__(self):
        import HanoverGame

        # Test 1: Wheaton; Timken Gymnasium; Wooster, Ohio; 3/1/19; L 73-84
        wheaton_url = "https://hanover.prestosports.com/sports/mbkb/2018-19/boxscores/20190301_0i35.xml"
        vs_wheaton = HanoverGame.HanoverGame(wheaton_url)
        print(vs_wheaton)
        self.assertEqual("Timken Gymnasium; Wooster, Ohio", vs_wheaton.location)
        self.assertEqual("March 1, 2019", vs_wheaton.date)
        self.assertEqual("Wheaton", vs_wheaton.opponent)
        self.assertEqual("73", vs_wheaton.hanover_score)
        self.assertEqual("84", vs_wheaton.opponent_score)

        # Test 2: Butler; Indianapolis, Ind. -- Hinkle Fieldhouse; 10/28/2017; L 36-68
        butler_url = "https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171028_m0c1.xml"
        vs_butler = HanoverGame.HanoverGame(butler_url)
        print(vs_butler)
        self.assertEqual("Indianapolis, Ind. -- Hinkle Fieldhouse", vs_butler.location)
        self.assertEqual("October 28, 2017", vs_butler.date)
        self.assertEqual("Butler", vs_butler.opponent)
        self.assertEqual("36", vs_butler.hanover_score)
        self.assertEqual("68", vs_butler.opponent_score)

        # Test 3: Rose-Hulman; Collier Arena -- Hanover, Ind.; 1/3/2018; L 69-71
        rose_url = "https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180103_eo0h.xml"
        vs_rose = HanoverGame.HanoverGame(rose_url)
        print(vs_rose)
        self.assertEqual("Collier Arena -- Hanover, Ind.", vs_rose.location)
        self.assertEqual("January 3, 2018", vs_rose.date)
        self.assertEqual("Rose-Hulman", vs_rose.opponent)
        self.assertEqual("69", vs_rose.hanover_score)
        self.assertEqual("71", vs_rose.opponent_score)

        # Test 4: Defiance; Collier Arena (Hanover, IN); 12/15/2018; W 77-72
        defiance_url = "https://hanover.prestosports.com/sports/mbkb/2018-19/boxscores/20181215_avgd.xml"
        vs_defiance = HanoverGame.HanoverGame(defiance_url)
        print(vs_defiance)
        self.assertEqual("Collier Arena (Hanover, IN)", vs_defiance.location)
        self.assertEqual("December 15, 2018", vs_defiance.date)
        self.assertEqual("Defiance", vs_defiance.opponent)
        self.assertEqual("77", vs_defiance.hanover_score)
        self.assertEqual("72", vs_defiance.opponent_score)
