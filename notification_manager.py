import smtplib
from decouple import config

MY_EMAIL = config('MY_EMAIL')
MY_PASSWORD = config('MY_PASSWORD')

class NotificationManager:

    def send_email(self, email_to, email_text):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email_to,
                msg=email_text.encode('utf-8')
            )

