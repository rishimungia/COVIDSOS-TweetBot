import requests

#COVID API
url = "https://covid-19-tracking.p.rapidapi.com/v1/india"

headers = {
    'x-rapidapi-key': "f8198b5227mshae93178c81a59d3p140b3ajsn78e5a5795fd7",
    'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
}

covidresponse = requests.request("GET", url, headers=headers)

coviddata = covidresponse.json()
status_text="Total Active cases: "+ coviddata['Active Cases_text']+" \n"+"New cases today: "+ coviddata['New Cases_text']+" \n"+"Total recovered: "+ coviddata['Total Recovered_text']