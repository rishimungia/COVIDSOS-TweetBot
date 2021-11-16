import tweepy
from modules.globalModule import *

def search_by_tag():
    temptxt="Enter a # to continue"
    saytext(temptxt)
    tag=input()
    tag="#"+tag
    saytext("Enter number of result you want: ")
    results=int(input())
    tagtimeline=tweepy.Cursor(api.search,q=tag,count=results,tweet_mode = "extended",lang="en",since="2021-04-04").items()
    for cases, tweet in enumerate(tagtimeline, start=1):
        print(cases,": ")
        print (tweet.created_at, tweet.full_text)
        if cases == results:
            break
        print("\n")

def search_by_user_name():
    saytext("Enter a user name")
    user_name=input()
    saytext("Enter number of result you want: ")
    results=input()
    usertimeline = api.user_timeline(screen_name=user_name,count=results,tweet_mode = "extended")
    for result, i in enumerate(usertimeline, start=1):
        print(result,":")
        print(i.full_text)
        print("\n")