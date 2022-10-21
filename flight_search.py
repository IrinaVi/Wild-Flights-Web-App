from urllib.request import urlopen
import requests
from amadeus import Client, ResponseError, NetworkError
import ssl
import datetime
from decouple import config

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

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
    #This class is responsible for talking to the Flight Search API.
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

    def flight_inspiration(self, origin, max_price):
        try:
            response = amadeus.shopping.flight_destinations.get(origin=origin, oneWay=False, nonStop=False, viewBy="COUNTRY", maxPrice=max_price)
            all_offers = response.data
            print("------------------")
            print(all_offers)
            print("------------------")
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
        except:
            print("Oops! error occurred.")
            return None

    def look_for_flight(self, city_code):
        tomorrow = datetime.date.today()+datetime.timedelta(1)
        tomorrow_format = tomorrow.strftime(f"%d/%m/%Y")
        six_months_later = tomorrow + datetime.timedelta(180)
        six_months_later_format = six_months_later.strftime(f"%d/%m/%Y")
        flight_endpoint = f"{TEQUILA_ENDPOINT}/search"
        headers = {"apikey": TEQUILA_API}
        try:
            parameters = {
                #can change fly from to UK
                "fly_from": "UK",
                #add multiple values from all users - city codes. Change city_code to arg
                "fly_to": city_code,
                "date_from": tomorrow_format,
                "date_to": six_months_later_format,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "curr": "GBP",
                "max_stopovers": 0,
                "sort": "price",
                "asc": 1
            }
            response = requests.get(url=flight_endpoint, params=parameters, headers=headers)
            flight_data = {
                "price": response.json()['data'][0]['price'],
                "departure_city": response.json()['data'][0]['cityFrom'],
                "departure_code": response.json()['data'][0]['cityCodeFrom'],
                "arrival_city": response.json()['data'][0]['cityTo'],
                "arrival_code": response.json()['data'][0]['cityCodeTo'],
                "outbound_date": datetime.datetime.fromtimestamp(response.json()['data'][0]['dTime']),
                "inbound_date": datetime.datetime.fromtimestamp(response.json()['data'][0]['aTime'])
            }
            print('-------------------------')
            print(flight_data)
            print('-------------------------')
            return flight_data

        except IndexError:
            parameters = {
                "fly_from": "UK",
                "fly_to": city_code,
                "date_from": tomorrow_format,
                "date_to": six_months_later_format,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "curr": "GBP",
                "max_stopovers": 4,
                "sort": "price",
                "asc": 1
            }
            response = requests.get(url=flight_endpoint, params=parameters, headers=headers)
            flight_data = {
                "price": response.json()['data'][0]['price'],
                "departure_city": response.json()['data'][0]['cityFrom'],
                "departure_code": response.json()['data'][0]['cityCodeFrom'],
                "arrival_city": response.json()['data'][0]['cityTo'],
                "arrival_code": response.json()['data'][0]['cityCodeTo'],
                "outbound_date": datetime.datetime.fromtimestamp(response.json()['data'][0]['dTime']),
                "inbound_date": datetime.datetime.fromtimestamp(response.json()['data'][0]['aTime'])
            }
            print('-------------------------')
            print(flight_data)
            print('-------------------------')
            return flight_data
        except:
            print(f"There were no flights found for {city_code}")