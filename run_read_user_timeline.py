# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:59:35 2020

@author: htadayyon
"""

from read_user_timeline import read_user_timeline
import pickle
import os
import pandas as pd

office = ['Microsoft365','MSFTDynamics365','linkedin']
computing = ['Xbox','surface','windows']
cloud = ['Azure','SQLServer','windowsserver','github']

tweets_office=[]
for thandle in office:
    if(os.path.isfile(thandle+'tweets_fullsearch.sav')==False):
        print('Extracting timeline for ' +thandle)
        read_user_timeline(thandle, 'fullsearch')
        tweets_office.append(pickle.load(open(thandle+'tweets_fullsearch.sav','rb')))
    else:
        print('Loading previously extracted timeline for ' + thandle)
        tweets_office.append(pickle.load(open(thandle+'tweets_fullsearch.sav','rb')))
        
        
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