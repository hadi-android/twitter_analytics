# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:07:44 2020

@author: htadayyon
"""

import pickle
import json
import pandas as pd
from twitter import *
from searchtweets import load_credentials, gen_rule_payload, collect_results

def read_user_timeline(name='',
                       from_date= pd.to_datetime('2020-1-1'), 
                       to_date=pd.to_datetime('2020-9-1'), 
                       method='tweepy'):
    
    if method == 'fullsearch':
        premium_search_args = load_credentials(".twitter_keys.yaml", account_type = "premium", env_overwrite=False)
        rule = gen_rule_payload("from:"+name,
                            from_date=str(from_date.strftime('%Y-%m-%d')), #UTC 2017-09-01 00:00
                            to_date=str(to_date.strftime('%Y-%m-%d')),
                            results_per_call=100)
        tweets = collect_results(rule,
                             max_results=100,
                             result_stream_args=premium_search_args) # change this if you need to
    
        
    elif method == 'tweepy':
        creds = json.load(open("twitter_credentials.json", "r"))       
        api = Twitter(auth=OAuth(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'], creds['CONSUMER_KEY'], creds['CONSUMER_SECRET']))
        n=10
        for i in range(n):
            if(i==0):
                tweets = api.statuses.user_timeline(screen_name="@"+name, count=400)
                last_id = tweets[-1]['id']
            else:
                t = api.statuses.user_timeline(screen_name="@"+name, count=400, max_id=last_id)
                last_id = t[-1]['id']
                tweets.extend(t)
                
                
        pickle.dump(tweets, open(name+'tweets.sav','wb'))    
        
    return tweets
        
            
    