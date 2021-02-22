import json
import pandas as pd
from .request_jhu import Request_JHU_US

request = Request_JHU_US()

def get_all_data():
    """
    Get all the data
    """
    concerned_columns = ['Province_State', 'Country_Region','Confirmed', 'Deaths', 'Recovered', 'Active', 'Total_Test_Results', 'People_Hospitalized', 'Incident_Rate', 'Case_Fatality_Ratio', 'Testing_Rate']
    result = pd.DataFrame(request.get_data_daily_reports(), columns=concerned_columns)
    
    return result.to_json(orient="index")


def get_all_data_by_category(category, province_name):
    """
    Get the data with the history
    """
    result = pd.DataFrame(request.get_data_time_series(category))
    rows = result.loc[result['Province_State'] == province_name.title()]

    return rows.to_json(orient="index")
    