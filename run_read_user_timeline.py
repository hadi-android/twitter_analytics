# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:59:35 2020

@author: htadayyon
"""

from read_user_timeline import read_user_timeline
import pickle
import os
import pandas as pd
from datetime import date
import datetime
import re


office = ['Microsoft365','MSFTDynamics365','linkedin']
computing = ['Xbox','surface','windows']
cloud = ['Azure','SQLServer','windowsserver','github']

from_date = pd.to_datetime('2020-1-1', format='%Y-%m-%d')
to_date = pd.to_datetime('2020-8-31')

# str(from_date.strftime('%Y-%m-%d'))
#initialize oldest date to a date after from_date so the while loop will start
oldest_date = to_date

# str(to_date)
# str(to_date.strftime('%Y-%m-%d'))

# tweets_office=[]
# for thandle in office:
#     if(os.path.isfile(thandle+'tweets_fullsearch.sav')==False):
#         print('Extracting timeline for ' +thandle)
#         while (oldest_date>=from_date):
#             tweets = read_user_timeline(thandle, from_date, to_date, 'fullsearch')
#             dates = [t['created_at'] for t in tweets]
#             oldest_date = pd.to_datetime(dates).min().strftime('%Y-%m-%d')
#             to_date = pd.to_datetime(dates).max().strftime('%Y-%m-%d')
#             pickle.dump(tweets, open(thandle+'_tweets_fullsearch_'+str(oldest_date)+'-'+str(to_date) +'.sav','wb')) 
#             to_date = pd.to_datetime(dates).min()
#             oldest_date = pd.to_datetime(dates).min().replace(tzinfo=None)

#         # tweets_office.append(pickle.load(open(thandle+'tweets_fullsearch.sav','rb')))
#     else:
#         print('Loading previously extracted timeline for ' + thandle)
#         tweets_office.append(pickle.load(open(thandle+'tweets_fullsearch.sav','rb')))

tweets = read_user_timeline('Microsoft365', pd.to_datetime('2020-1-1'), pd.to_datetime('2020-1-17'), 'fullsearch')


all_tweets=[]
regex = re.compile('Microsoft365_tweets_fullsearch_.*\.sav')
rootdir = os.getcwd()

for root, dirs, files in os.walk(rootdir):
  for file in files:
    if regex.match(file):
        all_tweets.append(pickle.load(open(file,'rb')))
        print(file)
        
date_range = []
date_list = []
text_list = []
reply_list = []
for i in range(len(tweets_office)):
    dates = [t['created_at'] for t in tweets_office[i]]
    dates = pd.to_datetime(dates)
    date_list.append(dates)
    text = [t['text'] for t in tweets_office[i]]
    text_list.append(text)
    reply = [t['in_reply_to_status_id'] for t in tweets_office[i]]
    reply_list.append(reply)
    tmp=[]
    tmp.append(dates.min())
    tmp.append(dates.max())
    date_range.append(tmp)
    
df = pd.DataFrame(date_list[0], columns=['Date'])   
df['Text'] = text_list[0]
df['reply'] = reply_list[0]

df.head(10)

df = df[df.reply.isnull()]

df.to_csv('Microsoft365_fullsearch.csv', index=False)


dates.min()
dates.min().strftime('%Y-%m-%d')
