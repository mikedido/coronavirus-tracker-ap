from . import Request

class Request_JSON(Requet):
    """
    Request the csv data    
    """
    def __init__(self):
        self.date = (datetime.now() - timedelta(days=1)).strftime('%m-%d-%Y')

    def execute(self, url):
        try:
            if 200 == requests.get(url).status_code :
                #return csv.reader(requests.get(url).text.splitlines(), delimiter=';')
            else :
                return ''
        except:
            pass