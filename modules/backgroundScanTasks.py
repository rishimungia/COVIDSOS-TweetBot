from threading import *
import time

from modules.globalModule import *
from modules.covidDM import covid_dm
from modules.checkMentions import check_mentions

# thread for background scans of mentions and DMs
class scan_thread(Thread):
    def run(self):
        while True:
            check_mentions()
            covid_dm()
            if(not threadstatus):
                break
            time.sleep(90)

t1 = scan_thread() # initilize thread