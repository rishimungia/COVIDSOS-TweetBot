from modules.globalModule import *
from modules.covidAPI import coviddata

# outputs covid data fetched from API
def covid_data():
    saytext("Total Active cases: "+ coviddata['Active Cases_text'])
    saytext("New cases today: "+ coviddata['New Cases_text'])
    saytext("Total recovered: "+ coviddata['Total Recovered_text'])