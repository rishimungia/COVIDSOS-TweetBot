from modules.globalModule import *

# output #COVIDSOS requirement
def search_sos():
    saytext("Enter location and requirment")
    req=input()
    saytext("Enter number of result you want: ")
    noq=input()
    sos_result=api.search(q=req,count=noq,tweet_mode = "extended",hashtag="#coronasos")
    for result,i in enumerate(sos_result,start=1):
        print(result,":")
        print(i.created_at)
        print("text:"+i.full_text)
        print("LINK: https://twitter.com/R_TweetBot/status/"+i.id_str)
        print("\n")