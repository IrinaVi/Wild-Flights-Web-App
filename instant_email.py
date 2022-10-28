from notification_manager import NotificationManager

notification_manager = NotificationManager()

def send_instant_email(email_to, name, flights):
    if flights != []:
        text = f"Subject: Cheap flights from {flights[0]['Origin']}! \n\n" \
               f"Hi, {name}! " \
               f"Here is some inspiration where you can fly from {flights[0]['Origin']}. "
        ending = "Sincerely, Wild Flights team"

        for i in range(1, len(flights)):
            flight_text = f"Fly to {flights[i]['Destination']} on the {flights[i]['Departure Date']} " \
                          f"and return on the {flights[i]['Return Date']} " \
                          f"just for {flights[i]['Price']}! "
            text += flight_text

        text += ending
    else:
        text = f"Subject: Sorry, no flights available! \n\n" \
        f"TEst test"
    notification_manager.send_email(email_to, text)
