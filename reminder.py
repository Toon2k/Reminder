import smtplib
from twilio.rest import Client
import os

MY_EMAIL = "pyemailtest33@gmail.com"
MAIL_PW = os.environ.get("MAIL_PW")
TO_MAIL = "janiswelsch@gmail.com"
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")


class Reminder:
    def __init__(self, message):
        self.message = message
        self.MY_EMAIL = "pyemailtest33@gmail.com"
        self.MAIL_PW = os.environ.get("MAIL_PW")
        self.TO_MAIL = "janiswelsch@gmail.com"
        self.API_KEY = os.environ.get("API_KEY")
        self.AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
        self.ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
        # Telefonnummern als ev's einbinden

    # -------------------- sent Message as Email -------------------- #
    def send_mail(self):
        utf_message = self.message.encode(encoding="UTF-8", errors="strict")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.MAIL_PW)
            connection.sendmail(
                from_addr=self.MY_EMAIL,
                to_addrs=self.TO_MAIL,
                msg=utf_message
            )

    # -------------------- sent Message as SMS -------------------- #
    # def send_sms(self):
    #     self.client = Client(ACCOUNT_SID, AUTH_TOKEN)  #ins init?
    #     self.sms = self.client.messages.create(
    #         body=self.message,
    #         from="+12762997306",
    #         to="+4915208732044",
    #     )

