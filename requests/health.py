from urllib2 import urlopen, Request
import json
import urllib2
import pandas as pd
from functions import haversine


class RequestHealth:

    def __init__(self):
        pass

    """
        Get information about the health in a community
    """
    def get_data(self):
        url = "https://data.cityofchicago.org/resource/iqnk-2tcu.json"
        data = urllib2.urlopen(url)

        #Tricky part
        result = json.load(data)
        aux = json.dumps(result)
        aux2 = json.dumps(json.loads(aux))

        #Data Frame
        data_frame =  pd.read_json(aux2)
        data_frame = data_frame.dropna()

        return data_frame
