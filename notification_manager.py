import smtplib

account_sid = ""
auth_token = ""

my_email = "bipboopbipbap@gmail.com"
password = ""

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

