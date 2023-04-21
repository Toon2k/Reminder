import datetime
from db_manager import DB_Manager
from reminder import Reminder


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
    print(message)

# -------------------- sent Message -------------------- #
reminder = Reminder(message)
reminder.send_mail()


# TODO: check weather for frost and rain and send reminder to protect plants / not having to water during summer

# TODO: create a class (Reminder) that send's different messages (Mail, SMS, Whatsapp)
