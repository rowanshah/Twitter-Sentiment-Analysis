import tweepy
from textblob import TextBlob

consumer_key = 'to9SXQQjhDSOdptpZa5wNKpSO'
consumer_key_secret = 'u8XMH5OYc5oQh3igbBO59ZOjQRj9uekUiVNUgdTiTnSewsEdYP'
access_token = '1205807190361153537-E09RCWOOBynFVofLw61ZfkAun2EgSx'
access_token_secret = 'aunh6iie4TKVrrcyB2OCCgY1erO1T02z78RM7ZQjMAmzG'


auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Arsenal')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print ('Positive')
	else:
		print ('Negative')
	print("")