# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:15:17 2019

@author: abhis
"""

#Group Members: Omkar Thorat and Abhishek Bhave


import tweepy
import csv
import pandas as pd
import datetime
x=datetime.datetime.now()
    

#https://stackoverflow.com/questions/38872195/tweepy-exclude-retweets

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def tweets(hashtag,no):
    msgs=[]
    for tweet in tweepy.Cursor(api.search, q=hashtag,rpp=100).items(no):
        #before appending check here    
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            msgs.append(tweet.text)
        tweet=pd.DataFrame(msgs)
        st=hashtag+x.strftime("%m-%d") +'.csv'
        tweet.to_csv(st)

#tweets('border wall',15000)
api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets('trumpwall',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets('mexico wall',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets('no border wall',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets('illegal immigration',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)
#
#tweets('border fence',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets('build the wall',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets('finish the wall',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets('the wall',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets('us mexico border',15000)
#api = tweepy.API(auth, wait_on_rate_limit=True)

tweets('shutdown',15000)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets('federal employees',15000)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets('migrant caravan',15000)
api = tweepy.API(auth, wait_on_rate_limit=True)


tweets('daca',15000)
api = tweepy.API(auth, wait_on_rate_limit=True)



    
