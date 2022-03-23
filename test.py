import requests
import datetime

AMADEUS_ENDPOINT = "http://test.api.amadeus.com/v2"
API_KEY = "PXkTSmD7GyxoCArWNTOIovxURzXOxqxT"
API_SECRET = "KfkHcWa7zO6YdGjD"
ACCESS_TOKEN = "N13JbJzZtzk9yHzeIpVks8M9goIi"

    #This class is responsible for talking to the Flight Search API.
def get_iata_code(self, city_name):
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    headers = {"apikey": TEQUILA_API}
    query = {"term": city_name, "location_types": "city"}
    response = requests.get(url=location_endpoint, headers=headers, params=query)
    results = response.json()["locations"]
    code = results[0]["code"]
    return code

        #change city_code to *args
def look_for_flight(city_code):
    tomorrow = datetime.date.today()+datetime.timedelta(1)
    tomorrow_format = tomorrow.strftime(f"%d/%m/%Y")
    six_months_later = tomorrow + datetime.timedelta(180)
    six_months_later_format = six_months_later.strftime(f"%d/%m/%Y")
    flight_endpoint = f"{AMADEUS_ENDPOINT}/shopping/flight-dates"
    headers = ACCESS_TOKEN
    parameters = {
            #can change fly from to UK
        "origin": "LON",
            #add multiple values from all users - city codes. Change city_code to arg
        "destination": city_code,
        }
    response = requests.get(url=flight_endpoint, params=parameters, headers=headers)
    print(response.json())

look_for_flight("PUJ")