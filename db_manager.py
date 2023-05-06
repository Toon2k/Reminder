import mysql.connector
import os

DBPW = os.environ.get("DBPW")


class DB_Manager:

    def __init__(self, db_name):
        self.db_name = db_name
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DBPW,
            database=self.db_name
        )

        self.mycursor = self.mydb.cursor()


# -------------------- create Table -------------------- #
    def create_table(table_name):
        self.mycursor.execute(f"CREATE TABLE {table_name}("
                         "ID INT AUTO_INCREMENT PRIMARY KEY,"
                         " Datum VARCHAR(255),"
                         " Bezeichnung VARCHAR(255),"
                         " Nachricht MEDIUMTEXT)")

        self.mycursor.execute("show tables")
        for x in self.mycursor:
            print(x)


