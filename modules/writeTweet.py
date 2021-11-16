from modules.globalModule import *

# for sending new Tweet
def write_tweet():
    saytext("Enter text below")
    text=input()
    api.update_status(text)
    saytext("Tweeted")