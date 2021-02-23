import json
import pandas
from .request_insee import Request_data, Request_data_depistage, Request_data_vaccination


request_data = Request_data()
request_depistage = Request_data_depistage()
Request_vaccination = Request_data_vaccination()

def get_data_vaccination():
    """
    Get all the centre de vaccination
    """
    print(Request_vaccination.get_location())
    pass

def get_data_hospitalisation():
    pass


def get_data_depistage():
    """
    Get all the centre dépistage
    """
    result = pandas.DataFrame(request_depistage.get_data())
    print(result)


def get_data():
    concerned_columns = ['date']
    result = pandas.DataFrame(request_data.get_data())
    print(result)
    
    #return json.loads(result.to_json(orient="index"))