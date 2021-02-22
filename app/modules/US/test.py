import csv
import requests
import json
from datetime import datetime, timedelta

class Request_CSV:
    """
    Request the csv data    
    """
    def __init__(self):
        self.date = (datetime.now() - timedelta(days=1)).strftime('%m-%d-%Y')

    def execute(self, url):
        if 200 == requests.get(url).status_code :
            return csv.reader(requests.get(url).text.splitlines(), delimiter=';')
        else :
            return ''


class Request_data_hospital(Request_CSV):

    #sURL = "https://static.data.gouv.fr/resources/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/20210131-192021/covid-hospit-incid-reg-2021-02-01-19h20.csv"
    URL ="https://static.data.gouv.fr/resources/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/20210201-192042/covid-hospit-incid-reg-2021-02-01-19h20.csv"

    def get_daily(self):
        return super().execute(self.URL)
    
    def get_total(self):
        return super().execute(self.URL)


class Request_data(Request_CSV):
    URL = "https://static.data.gouv.fr/resources/donnees-relatives-a-lepidemie-de-covid-19-en-france-vue-densemble/20210202-153109/synthese-fra.csv"

    def get_data(self):
        return super().execute(self.URL)



class Request_data_vaccination(Request_CSV):
 
    URL = "https://static.data.gouv.fr/resources/lieux-de-vaccination-contre-la-covid-19/20210202-150506/centres-vaccination.csv" 

    def get_location(self):
        return super().execute(self.URL)




#TEST MAIN
for row in Request_data_hospital().get_daily() :
    print(row)

for row in Request_data().get_data():
    print(row)

for row in Request_data_vaccination().get_location():
    print(row)