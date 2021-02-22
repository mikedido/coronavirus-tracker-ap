import json
import pandas
from .request_insee import Request_data, Request_data_depistage


request_data = Request_data()
request_depistage = Request_data_depistage()

def get_data_vaccination():

    pass

def get_data_hospitalisation():
    pass


def get_data():
    concerned_columns = ['date']
    result = pandas.DataFrame(request_data.get_data())
    print(result)
    
    #return json.loads(result.to_json(orient="index"))