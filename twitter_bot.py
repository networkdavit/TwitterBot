import tweepy
import time
import threading


consumer_key = "" #please enter your key here
consumer_secret = "" #please enter your key here
access_token = "" #please enter your key here
access_token_secret = "" #please enter your key here

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True) 
user = api.get_user('') #please enter your username here
public_tweets = api.home_timeline()

all_tweets = []
bot = True

tweet_list = []

def delay(seconds, tweet):
	time.sleep(seconds)
	api.update_status(tweet)

def tweet(input):	
	api.update_status(input)


def post_tweets():
	global post_delay
	post_delay = post_delay
	for tweet in tweet_list:
		t = threading.Thread(target=delay, args = (post_delay, tweet,))
		t.start()
		post_delay += post_delay

