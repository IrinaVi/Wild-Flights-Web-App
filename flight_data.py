tomorrow = datetime.date.today() + datetime.timedelta(1)
tomorrow_format = tomorrow.strftime(f"%d/%m/%Y")
new_date = "15/01/2022"
delta = relativedelta(months=6)
six_months_later = tomorrow + delta
six_months_later_format = six_months_later.strftime(f"%d/%m/%Y")

class FlightData:

    def __init__(self, city_code, tomorrow, six_months_later):
        self.fly_from = "LON"
        self.fly_to = city_code
        self.date_from = tomorrow
        self.date_to = six_months_later
        self.nights_in_dst_from = 7

        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "adults": 2,
        "price_to": max_price,
        "curr": "GBP",
        "max_stopovers": 0,
        "sort": "price",
        "asc": 1