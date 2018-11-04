from TwitterFollowBot import TwitterBot
from numpy.random import *

def favmain():
    my_bot = TwitterBot()
    my_bot.auto_fav("モンスト", count=30)

while True:
    favmain()
    time.sleep(21600)
