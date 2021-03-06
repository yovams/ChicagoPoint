from irequest import IRequest
from urllib2 import urlopen, Request
import json
import urllib2
import pandas as pd
from functions import haversine
import os

class RequestCost(IRequest):

    def __init__(self):
        self.name = "static/json/cost_rent.json"
        self.url = os.path.join(os.path.dirname(__file__),"../", self.name)
        self.cost_neighborhood = self.get_data()


    def get_instance_data(self):
        """ Get the instance of this class """
        return self.cost_neighborhood


    def get_data(self):
        """ Create data frame cost by neighborhood """
        try:
            data = open(self.url, "r+")

            result = json.load(data)
            aux = json.dumps(result)
            aux2 = json.dumps(json.loads(aux))

            #Data Frame
            data_frame =  pd.read_json(aux2)
            data_frame = data_frame.dropna()
            return data_frame
        except Exception as e:
            print("error")
            return []


    def get_cheapest_comunities(self,n = 5):
        """ Get most cheapest comunities by default 5 """
        try:
            info = self.cost_neighborhood[["community_area", "cost1bedroom", "cost2bedrooms"]]
            cheapest =  info.nsmallest(n, 'cost1bedroom')
            info_js = cheapest.to_json()
            aux = json.loads(info_js)

            keyse = "community_area"
            zipse = "cost1bedroom"
            ad = "cost2bedrooms"
            dataset = []
            for ar in aux[zipse]:
                url = aux[keyse][ar]
                _zip = aux[zipse][ar]
                _ad = aux[ad][ar]
                dataset.append([url, _zip, _ad])
                return dataset
        except Exception as e:
            print("error")
            return []



    def get_cost_table_neighborhood(self):
        """ Get the table of cost by neighborhood. """
        try:
            info = self.cost_neighborhood[["community_area", "cost1bedroom", "cost2bedrooms"]]
            info_js = info.to_json()
            aux = json.loads(info_js)

            keyse = "community_area"
            zipse = "cost1bedroom"
            ad = "cost2bedrooms"
            dataset = []
            for ar in aux[zipse]:
                url = aux[keyse][ar]
                _zip = aux[zipse][ar]
                _ad = aux[ad][ar]
                dataset.append([url, _zip, _ad])
                return dataset
        except Exception as e:
            print("error")
            return []
