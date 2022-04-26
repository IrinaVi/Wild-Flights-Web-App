import smtplib

account_sid = "AC4f2db0ae0b0a12337d14493b8b8bab03"
auth_token = "d6b6a89910597c83c875344f3aa868e4"

my_email = "bipboopbipbap@gmail.com"
password = "hog-GH7893!d!0s"

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

