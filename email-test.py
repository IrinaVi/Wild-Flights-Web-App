from notification_manager import NotificationManager
email_to = 'irinavik1805@gmail.com'
text="TEST"

messanger = NotificationManager()
messanger.send_email(email_to=email_to, email_text=text)