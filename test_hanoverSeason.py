from unittest import TestCase


class TestHanoverSeason(TestCase):
    def test___init__(self):
        import HanoverSeason
        import HCMBB_Stats

        # Test 1: 2017-2018; 10/28/2017-3/2/2018
        season_year = 2018
        seasons_dict = HCMBB_Stats.get_game_url_dict()
        season_2018 = HanoverSeason.HanoverSeason(season_year, seasons_dict)
        print(season_2018)
        self.assertEqual("2017-2018", season_2018.season_id)
        self.assertEqual("10/1/2017", season_2018.start_date)
        self.assertEqual("3/31/2018", season_2018.end_date)

