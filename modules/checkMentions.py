from modules.globalModule import api, saytext
from modules.covidDM import add_to_dm

greetings = ['hi', 'hello', 'hey']

lastseen_file='modules/data/lastseen.txt'
unchecked_file = 'modules/data/unchecked.txt'

# check for last seen tweet
with open(lastseen_file, 'r') as file_read:
    lastseen_id = int(file_read.read().strip())

# handle new mentions on timeline (for pre-defined hashtags)
def check_mentions():
    if lastseen_id != 00:
        tweets = api.mentions_timeline(lastseen_id, tweet_mode='extended')
    else:
        tweets = api.mentions_timeline(tweet_mode='extended')
    
    for tweet in reversed(tweets):
        if '#like' in tweet.full_text.lower():
            api.create_favorite(tweet.id)
        if '#reply' in tweet.full_text.lower():
            api.update_status("@" + tweet.user.screen_name + " This is an Auto Generated Reply from TweetBot", tweet.id)
        if '#coviddm' in tweet.full_text.lower() and 'start' in tweet.full_text.lower():
            add_to_dm(tweet)
        if any(x in tweet.full_text.lower() for x in greetings):
            api.update_status("@" + tweet.user.screen_name + " Hey!", tweet.id)
        else:
            with open(unchecked_file, 'a') as file_write:
                file_write.write(str(tweet.id)+"\n")
        with open(lastseen_file, 'w') as file_write:
            file_write.write(str(lastseen_id))

# handle new mentions (not handeled by pre-defined hashtags)
def checkunreplied():
    def updatefile(uncheck_file, tweet):
        with open(unchecked_file, "w") as f:
            for line in uncheck_file:
                if line.strip("\n") != str(tweet.id):
                    f.write(line)
    
    uncheck_file = open(unchecked_file, 'r+')
    for line in uncheck_file:
        tweet = api.get_status(line)
        saytext(tweet.user.screen_name +" "+ tweet.text)
        saytext("What do you want to do? [reply or leave]")
        reply_input=input()
        if reply_input== 'reply':
            saytext("Enter text below: ")
            reply_text=input()
            api.update_status("@" + tweet.user.screen_name +" "+ reply_text, tweet.id)
            updatefile(uncheck_file, tweet)
        else:
            updatefile(uncheck_file, tweet)
            continue