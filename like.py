
# -*- coding:utf-8 -*-

#Tweepyのインポート
import tweepy
from time import sleep

#keyの取得
CONSUMER_KEY = 	'cFSfMvnyEdbOdiUt3DP76GkAg'
CONSUMER_SECRET = 'qhXU3K6g1xTX66E4vNYUdtGj4pe38iIYWJ8Xd8u32gQlfmmI1a'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '1394962950-APVDSitxXyToODdmKT2NIJvjulUPd2wPpZVn6RG'
ACCESS_SECRET = 'NSoxHS3Q5AlTrVAC6jcWW92I9AI8Udz3SskSniCeSmZ0S'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

q = ("モンスト　lang:ja source:twitter_for_android OR lang:ja source:twitter_for_iphone")
count = 1
search_results = api.search(q=q, count=count)
for result in search_results:
    screen_id = result.user._json['screen_name']
    print(screen_id+"をフォローしました")
    api.create_friendship(screen_id)
