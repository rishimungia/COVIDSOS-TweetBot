import json

from modules.covidAPI import *
from modules.globalModule import *

dmlist_file= "modules/data/dmlist.txt" # stores user IDs for DM service
element='DM_LIST'

# function to check if user is enrolled in DM service database
def check_condition(uid):
    with open('dm_list.txt', 'r') as json_file:
        data = json.load(json_file)
        for user in data[element]:
            return bool(user['user_id']==uid and user['active'])

# function to add new user to DM service database
def add_dm_user(user_id):
    with open('dm_list.txt','r') as json_file:
        data = json.load(json_file)
        data['DM_LIST'].append({
            'user_id': user_id,
            'active': True
        })
    with open('dm_list.txt', 'w') as outfile:
        json.dump(data, outfile, indent=4)

# function to handle DM service enrollment tweet 
def add_to_dm(tweet):
    check_friend=api.show_friendship(source_screen_name = tweet.user.screen_name, target_screen_name = "R_TweetBot")
    if check_friend[0].following:
        if check_condition():
            api.update_status("@" + tweet.user.screen_name + " Already in DM list", tweet.id) # if user already enrolled
        else:
            add_dm_user(tweet.user.id_str)
            api.send_direct_message(tweet.user.id_str, "INSTRUCTIONS: \nSend covidstatus - recive the covid details \nSend covidsos [location] [requirement]- get covid sos tweet based on your location \nSend stop - stop getting messages")
            api.update_status("@" + tweet.user.screen_name + " Added to DM list", tweet.id)
    else:
        api.update_status("@" + tweet.user.screen_name + " Please follow to use this", tweet.id) # if user is not following bot account

# function to disable user from DM service
def remove_from_dm(user_id):
    with open('dm_list.txt', 'r') as json_file:
        data = json.load(json_file)
        for i, user in enumerate(data['DM_LIST']):
            if str(user_id) == str(user['user_id']):
                data['DM_LIST'][i]['active'] = False
                with open('dm_list.txt', 'w') as json_file:
                    json_file.write(json.dumps(data, indent=4))

# function to re-activate disabled user for DM service
def set_active_user(user_id):
    with open('dm_list.txt', 'r') as json_file:
        data = json.load(json_file)
        for i, user in enumerate(data['DM_LIST']):
            if str(user_id) == str(user['user_id']):
                data['DM_LIST'][i]['active'] = True
                with open('dm_list.txt', 'w') as json_file:
                    json_file.write(json.dumps(data, indent=4))

# function to handle DM service 
def covid_dm():  # sourcery no-metrics
    messages = api.list_direct_messages(count=5)
    for message in messages:
        sender_id = message.message_create["sender_id"]
        if sender_id!='1378697655744745481':
            with open(dmlist_file) as json_file:
                data = json.load(json_file)
                for user in data[element]:
                    text = message.message_create["message_data"]["text"]
                    if str(user['user_id'])==sender_id and user['active'] and sender_id!='1378697655744745481':
                            if text=='covidstatus':
                                api.send_direct_message(sender_id, status_text)
                            if text=='stop':
                                remove_from_dm(sender_id)
                                api.send_direct_message(sender_id, "stopped \nSend start to start again")
                            if 'covidsos' in text:
                                temp_text=text.split()
                                link_s="https://twitter.com/search?q=%23covidsos%20"+temp_text[1]+"%20"+temp_text[2]+"%20available"
                                api.send_direct_message(sender_id, link_s)
                            if text=='start':
                                api.send_direct_message(sender_id, "Already enabled")

                    else:
                        if text=='start':
                            set_active_user(sender_id)
                            api.send_direct_message(sender_id, "INSTRUCTIONS: \nSend covidstatus - recive the covid details \nSend covidsos [location] [requirement]- get covid sos tweet based on your location \nSend stop - stop getting messages")
                        continue
        else:
            break