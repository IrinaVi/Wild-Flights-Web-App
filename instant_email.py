from notification_manager import NotificationManager

notification_manager = NotificationManager()

def send_instant_email(email_to, name, flights):
    if flights != []:
        text = f"Subject: Cheap flights from {flights[0]['Origin']}! \n\n" \
               f"Hi, {name}! " \
               f"Here is some inspiration where you can fly from {flights[0]['Origin']}. \n\n"
        ending = "\n Sincerely, Wild Flights team"

        for i in range(0, len(flights)-1):
            flight_text = f"{i+1}. Fly to {flights[i]['Destination'][0]}, {flights[i]['Destination'][1]} on the {flights[i]['Departure Date']} " \
                          f"and return on the {flights[i]['Return Date']} " \
                          f"for just £{flights[i]['Price']}! \n"
            text += flight_text

        text += ending
    else:
        text = f"Subject: Sorry, no flights available! \n\n" \
        "This time the Wild Flights team was not able to find any flights from your city within the specified budget. " \
               "We send emails with the flights every Friday. \n\n" \
               "Sincerely, Wild Flights team"

    print("TEXT")
    print(text)
    print("TEXT")
    notification_manager.send_email(email_to, text)
