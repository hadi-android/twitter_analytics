# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:07:44 2020

@author: htadayyon
"""

from twitter import *
import json

def read_user_timeline(name):
    # Load credentials from json file
    creds = json.load(open("twitter_credentials.json", "r"))
    
    # api = twitter.Api(consumer_key=creds['CONSUMER_KEY'],
    #   consumer_secret=creds['CONSUMER_SECRET'],
    #   access_token_key=creds['ACCESS_TOKEN'],
    #   access_token_secret=creds['ACCESS_SECRET'],
    #   tweet_mode='extended')
    
    api = Twitter(auth=OAuth(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'], creds['CONSUMER_KEY'], creds['CONSUMER_SECRET']))
    
    # tweets = api.statuses.user_timeline(screen_name="microsoft", count=400)
    # tweets1 = api.statuses.user_timeline(screen_name='microsoft', count=400, max_id='1300490551729549313')
    
    # t = tweets[0]
    # t['id']
    
    #name = 'microsoft'
    n=10
    for i in range(n):
        if(i==0):
            tweets = api.statuses.user_timeline(screen_name=name, count=400)
            last_id = tweets[-1]['id']
        else:
            t = api.statuses.user_timeline(screen_name=name, count=400, max_id=last_id)
            last_id = t[-1]['id']
            tweets.extend(t)
            
    
    import pickle
    pickle.dump(tweets, open(name+'tweets.sav','wb'))        
            
    