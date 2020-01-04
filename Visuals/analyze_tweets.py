import json
import pandas as pd
import matplotlib.pyplot as plt
import re


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


def main():


	#Reading Tweets
	print 'Reading Tweets\n'
	tweets_data_path = 'twitter_data.txt'

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_data.append(tweet)
	    except:
	        continue


	#Structuring Tweets
	print 'Structuring Tweets\n'
	tweets = pd.DataFrame()
	tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)


	#Adding programming languages columns to the tweets DataFrame
	print 'Adding football team tags to the data\n'
	tweets['arsenal'] = tweets['text'].apply(lambda tweet: word_in_text('arsenal', tweet))
	tweets['chelsea'] = tweets['text'].apply(lambda tweet: word_in_text('chelsea', tweet))
	tweets['mancity'] = tweets['text'].apply(lambda tweet: word_in_text('mancity', tweet))


	#Analyzing Tweets by programming language: First attempt
	print 'Analyzing tweets by football team: First attempt\n'
	prg_langs = ['arsenal', 'chelsea', 'mancity']
	tweets_by_prg_lang = [tweets['arsenal'].value_counts()[True], tweets['chelsea'].value_counts()[True], tweets['mancity'].value_counts()[True]]
	x_pos = list(range(len(prg_langs)))
	width = 0.8
	fig, ax = plt.subplots()
	plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
	ax.set_ylabel('Number of tweets', fontsize=15)
	ax.set_title('Ranking: Teams(Raw data)', fontsize=10, fontweight='bold')
	ax.set_xticks([p + 0.4 * width for p in x_pos])
	ax.set_xticklabels(prg_langs)
	plt.grid()
	plt.savefig('tweet_by_football_teams_1.png', format='png')


if __name__=='__main__':
	main()
