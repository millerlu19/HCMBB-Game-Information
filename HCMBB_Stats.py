# HCMBB_Stats.py

import requests
from bs4 import BeautifulSoup
import HanoverGame.py

# Conference Games
Franklin_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180120_g0e4.xml')
Franklin_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171202_uidy.xml?view=boxscore')
Transy_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180124_8532.xml')
Transy_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171206_01gr.xml?view=boxscore')
Bluffton_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171209_lytk.xml?view=boxscore')
Bluffton_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180127_pw2q.xml')
Defiance_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180217_7z40.xml')
Defiance_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171216_mrxa.xml?view=boxscore')
Rose_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180103_eo0h.xml?view=boxscore')
Rose_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180131_4elz.xml')
Manchester_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180210_97g4.xml')
Manchester_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180106_90o3.xml?view=boxscore')
Earlham_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180110_4h64.xml?view=boxscore')
Earlham_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180207_wd9a.xml')
Anderson_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180203_tjz8.xml')
Anderson_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180113_anw0.xml?view=boxscore')
MSJ_Home = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180214_zfuq.xml')
MSJ_Away = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180117_83jv.xml?view=boxscore')

# Conference Tourney Games
Bluffton_Conf = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180220_yqr3.xml')
MSJ_Conf = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180223_7p1e.xml')
Rose_Conf = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180224_m8nh.xml')

# Non Conference Games
Butler = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171028_m0c1.xml')
KentState = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171117_26u3.xml')
Otterbein = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171118_h4fm.xml')
Spalding = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171121_6t9y.xml')
Wooster = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171125_q7io.xml')
OHWesleyan = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171129_5u6z.xml')
Marietta = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171229_3e67.xml')
OHChillicothe = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20171230_hohs.xml')
LeTourneau = requests.get('https://hanover.prestosports.com/sports/mbkb/2017-18/boxscores/20180302_liy0.xml')


def main():
    game_pages = [Butler, Otterbein, Spalding, Wooster, OHWesleyan, Franklin_Away, Transy_Away, Bluffton_Home, Defiance_Away, Marietta, OHChillicothe, Manchester_Away, Earlham_Home, Anderson_Away, MSJ_Away, Franklin_Home, Transy_Home, Bluffton_Away, Rose_Away, Anderson_Home, Earlham_Away, Manchester_Home, MSJ_Home, Defiance_Home, Bluffton_Home, MSJ_Conf, Rose_Conf, LeTourneau]
    game_list = []
    for url in game_pages:
        game_list.append(HanoverGame(url))

main()