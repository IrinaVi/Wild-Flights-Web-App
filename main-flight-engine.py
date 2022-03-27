import flight_search
from notification_manager import NotificationManager
from app import User, db
import psycopg2
import os

#DATABASE_URL = os.environ.get("postgresql://euviacqgmlflof:2364b9b4ccf7d5b38397f69f66e1b640422c36e31816c4f20cd54ce8f1a91642@ec2-52-201-124-168.compute-1.amazonaws.com:5432/d8lt7jnnfdvg1r")
#con = psycopg2.connect(DATABASE_URL)
#cur = con.cursor()

#list of all city codes:
total_users = len(db.session.query(User).all())
messanger = NotificationManager()

def my_function():
    for i in range(1,total_users+1):
        user = User.query.get(i)
        price = user.max_price
        search_for_flight = flight_search.FlightSearch()
        origin = search_for_flight.get_iata_code(user.fly_from)
        flight=search_for_flight.flight_inspiration(origin, price)
        email_to = user.email
        reciever = user.name
        print(user.email, origin, flight)
        if flight == None:
            text = f"Subject: Sorry, no suitable flights from your city  \n\n" \
                   f"Hi {reciever} \nUnfortunately, we did not find any flights from {user.fly_from} for the maximum price of ${user.max_price}. " \
                   f"We will keep looking and let you know as soon as something suitable available, stay tuned! " \
                   f"Alternatively, please visit our website and modify the search! " \
                   "Sincerely, Wild flights team"
            messanger.send_email(email_to=email_to, email_text=text)
        if flight != None:

            text = f"Subject: We've found where you could fly! \n\n" \
                f"Hi, {reciever}! Here is some inspiration where you can fly from {user.fly_from}. "
            ending = "Sincerely, Wild Flights team"

            for i in flight:
                dest_name = search_for_flight.get_city_name(i['Destination'])
                flight_text = f"Fly to {dest_name} on the {i['Departure Date']} and return on the {i['Return Date']} " \
                f"just for ${i['Price']}! " \
                f"Here is the link for more details: {i['Link']}. "

                text += flight_text
                print(text, flight_text)
            text+=ending
            messanger.send_email(email_to=email_to, email_text=text)
            print(text)

my_function()

