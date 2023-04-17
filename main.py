import datetime
from db_manager import DB_Manager
import os
import smtplib


MY_EMAIL = "pyemailtest33@gmail.com"
MAIL_PW = os.environ.get("MAIL_PW")
TO_MAIL = "janiswelsch@gmail.com"

timer = datetime.datetime.now()
today = timer.strftime("%d.%m.")


# -------------------- connect to DB -------------------- #
db_manager = DB_Manager("garten")


# -------------------- get Message from Table -------------------- #
sql = "SELECT * FROM todo WHERE Datum = %s"
val = ("15.03.",)
db_manager.mycursor.execute(sql, val)
myresult = db_manager.mycursor.fetchall()
if len(myresult) != 0:
    pflanze = myresult[0][0]
    text = myresult[0][2]
    # print(myresult)
    # print(text)
    # print(pflanze)
    message = f"Subject: todo für {pflanze}\n\n{text}"
    utf_message = message.encode(encoding="UTF-8", errors="strict")
    print(message)

# -------------------- sent Message as Email -------------------- #
def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MAIL_PW)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_MAIL,
            msg=utf_message
        )
        # connection.send

send_mail()

# TODO: check weather for frost and rain and send reminder to protect plants / not having to water during summer
