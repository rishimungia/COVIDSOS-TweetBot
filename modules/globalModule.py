import pyttsx3
from tweepy import OAuthHandler
import tweepy

from modules.tweetAuth import *

# setting twitter variable
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# setting text to speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')

# property setting
engine.setProperty('rate', 150)

# function for TTS output
def saytext(tptx):
    print(tptx)
    engine.say(tptx)
    engine.runAndWait()
    engine.stop()

threadstatus = False