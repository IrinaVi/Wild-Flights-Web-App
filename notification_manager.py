import smtplib

account_sid = "AC"
auth_token = "d"

my_email = "bipboopbipbap@gmail.com"
password = "h"

class NotificationManager:

    def send_email(self, email_to, email_text):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_to,
                msg=email_text
            )

