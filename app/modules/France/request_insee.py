import csv
import json
import pandas
import requests as r
from datetime import datetime, timedelta
from io import StringIO

class Request_CSV:
    """
    Request the csv data    
    """
    def __init__(self):
        self.date = (datetime.now() - timedelta(days=1)).strftime('%m-%d-%Y')

    def execute(self, url):
        data = r.get(url)
        if 200 == data.status_code :
            return csv.reader(data.text.splitlines(), delimiter=';')

    def execute_panda(self, url):
        data = r.get(url)

        if 200 == data.status_code :
            return pandas.read_csv(url)


class Request_data_hospitalisation(Request_CSV):

    URL ="https://static.data.gouv.fr/resources/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/20210201-192042/covid-hospit-incid-reg-2021-02-01-19h20.csv"

    def get_daily(self):
        return super().execute(self.URL)
    
    def get_total(self):
        return super().execute(self.URL)


class Request_data(Request_CSV):
    URL = 'https://www.data.gouv.fr/fr/datasets/r/2cfa819d-7b5e-4a4f-8f79-bf413ebb0cbf'

    def get_data(self):
        return super().execute(self.URL)


class Request_data_vaccination(Request_CSV):
    URL = "https://static.data.gouv.fr/resources/lieux-de-vaccination-contre-la-covid-19/20210222-100509/centres-vaccination.csv"

    def get_location(self):
        return super().execute(self.URL)


class Request_data_depistage(Request_CSV):
    URL = 'https://www.data.gouv.fr/fr/datasets/r/2cfa819d-7b5e-4a4f-8f79-bf413ebb0cbf'

    def get_data(self):
        return super().execute_panda(self.URL)