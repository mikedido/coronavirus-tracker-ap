import csv
import requests
import json
from . import Request
from datetime import datetime, timedelta

class Request_CSV(Request):
    """
    Request the csv data    
    """
    def __init__(self):
        self.date = (datetime.now() - timedelta(days=1)).strftime('%m-%d-%Y')

    def execute(self, url):
        try:
            if 200 == requests.get(url).status_code :
                return csv.reader(requests.get(url).text.splitlines(), delimiter=';')
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt) 