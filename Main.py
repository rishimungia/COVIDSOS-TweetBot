from modules.globalModule import *

from modules.writeTweet import write_tweet
from modules.checkMentions import checkunreplied
from modules.covidData import covid_data
from modules.searchTweet import search_by_tag, search_by_user_name
from modules.searchSOS import search_sos
from modules.backgroundScanTasks import t1

# bot start
saytext("Hi!")
saytext("Starting Tweet Bot")
threadstatus = True
t1.start()

while True:
    
    print("\nTweet Bot Menu")
    print("1. Make a Tweet")
    print("2. Check for unreplied Tweets")
    print("3. Covid Status")
    print("4. Search Tweets by #")
    print("5. Search Tweets by Username")
    print("6. Search for #COVIDSOS")
    print("7. Exit Tweet Bot")

    print("\nEnter your choice:")
    choise=int(input())
    
    if choise == 1:
        write_tweet()
    elif choise == 2:
        checkunreplied()
    elif choise == 3:
        covid_data()
    elif choise == 4:
        search_by_tag()
    elif choise == 5:
        search_by_user_name()
    elif choise == 6:
        search_sos()
    elif choise == 7:
        threadstatus = False
        t1.join()
        saytext("Good bye")
        break