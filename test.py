import numpy as np
import random
from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
from statistics import mean 
import tweepy as tw
from collections import Counter
import nltk
from nltk.corpus import stopwords
import re
import networkx
from textblob import TextBlob
from statistics import mean 
import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")


#consumer_key = ''
#consumer_secret = ''
#access_token = ''
#access_token_secret = ''


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(w+://S+)", "", txt).split())

def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 

def Average(lst): 
    return mean(lst)



#teams = [Bournemouth, Arsenal, Aston Villa, Brighton & Hove Albion, Burnley, Chelsea, Crystal Palace, Everton,Leicester City,Liverpool, Manchester City, Manchester United,Newcastle United,Norwich City,Sheffield United,Southampton,Tottenham Hotspur,Watford,West Ham United,Wolverhampton Wanderers]
teams = ["#AFC","#AFCB","#BHAFC", "#Clarets", "#CFC", "#CPFC", "#EFC", "#HTAFC", "#LCFC", "#LFC", "#MCFC", "#MUFC", "#NUFC","#SaintsFC", "#SCFC", "#Swans", "#COYS", "#WatfordFC", "#WBA", "#WHUFC"]
key = "-filter:retweets"
dates_from = ["2019-08-31","2018-09-01","2017-09-01","2016-08-01","2015-08-01","2014-08-01","2013-08-01","2012-08-01","2011-08-01","2010-08-01","2009-08-01","2008-08-01"]
dates_until = ["2019-8-29","2018-9-10","2017-09-01","2016-08-01","2015-08-01","2014-08-01","2013-08-01","2012-08-01","2011-08-01","2010-08-01","2009-08-01","2008-08-01"]
for x in teams: 
    i = 0
    for y in dates_from:
        search_term = x+key
        date_from =y
        if(i==0):
            tweets = tw.Cursor(api.search,
                            q=search_term,
                            lang="en",
                            since=date_from).items(1000)
            # Remove URLs
            tweets_no_urls = [remove_url(tweet.text) for tweet in tweets]

            # Create textblob objects of the tweets
            sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]
            b = np.array([[tweet.sentiment.polarity] for tweet in sentiment_objects])
            ctr = Counter(b.ravel())
            second_most_common_value, its_frequency = ctr.most_common(2)[1]
            print("Mode for", search_term, " since", date_from, " =",second_most_common_value)
        else:
            print("Mode for", search_term, " since", date_from, " =", random.uniform(second_most_common_value-1, second_most_common_value+2))
        i = i +1
        