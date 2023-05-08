import smtplib
from twilio.rest import Client
import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

    # -------------------- sent Message as WhatsAPP -------------------- #
    def send_whatsapp(self):
        url = "https://web.whatsapp.com/"
        chrome_driver_path = "C:/Users/janis/Desktop/Tools/Chrome Driver/chromedriver.exe"
        driver_service = Service(executable_path=chrome_driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")
        options.add_argument(r"--user-data-dir=C:\Users\janis\AppData\Local\Google\Chrome\User Data\Default")   # option --headless breaks it until restart!

        driver = webdriver.Chrome(service=driver_service, options=options)
        driver.get(url)
        time.sleep(4)

        receiver = driver.find_element(By.CSS_SELECTOR, "span[title='Janis Welsch']")
        receiver.click()
        time.sleep(2)

        text_input = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
        text_input.send_keys(f"{self.message}\ue007")
        time.sleep(1)

        driver.quit()
