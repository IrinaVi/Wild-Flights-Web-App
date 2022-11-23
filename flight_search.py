from urllib.request import urlopen
import requests
from amadeus import Client, ResponseError
import ssl
from decouple import config
from ratelimit import limits

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

ONE_DAY = 86400

def ssl_disabled_urlopen(endpoint):
    context = ssl._create_unverified_context()
    return urlopen(endpoint, context=context)

amadeus = Client(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    hostname='production',
    log_level='debug',
    http = ssl_disabled_urlopen
)

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API = config('TEQUILA_API')


class FlightSearch:
    def get_iata_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_city_name(self, iata_code):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API}
        query = {"term": iata_code, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        city_name = results[0]["name"]
        country = results[0]['country']['name']
        return [city_name, country]

    @limits(calls=10, period=ONE_DAY)
    def flight_inspiration(self, origin, max_price):
        try:
            response = amadeus.shopping.flight_destinations.get(origin=origin, oneWay=False, nonStop=False, viewBy="COUNTRY", maxPrice=max_price)
            all_offers = response.data
            flight_data = []
            for offer in all_offers:
                one_flight = {
                    "Departure city": origin,
                    "Destination": offer['destination'],
                    "Departure Date": offer['departureDate'],
                    "Return Date": offer['returnDate'],
                    "Price": offer['price']['total'],
                    "Link": offer['links']['flightDates']
                }
                flight_data.append(one_flight)
            return flight_data
        except ResponseError as error:
            print(f"Oops! {error} occurred.")
            return None
