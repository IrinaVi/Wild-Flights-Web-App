import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/135c140652258fa806d70f20aa9a4b37/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_prices(self):
        response = requests.get(SHEETY_ENDPOINT)
        return response.json()["prices"]