import os
import mysql.connector

DB_HOST = "flightdb"
DB_USER = "root"
DB_PASSWORD = "Lili-2022"
DB_NAME = "flightdb"

# Establish the database connection
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

class DataManager:
    def __init__(self):
        self.dest_info = []
        self.cx_info = []

    def get_dest_info(self):
        # Retrieve data from the MySQL database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM prices")
        self.dest_info = cursor.fetchall()
        cursor.close()
        return self.dest_info

    def update_dest_info_iata(self):
        # Update data in the MySQL database
        cursor = db.cursor()
        for dest in self.dest_info:
            sql = "UPDATE prices SET IATA = %s WHERE id = %s"
            val = (dest[2], dest[0])
            cursor.execute(sql, val)
            db.commit()
        cursor.close()

    # def get_cx_info(self):
    #     # Retrieve data from the MySQL database
    #     cursor = db.cursor()
    #     cursor.execute("SELECT * FROM users")
    #     self.cx_info = cursor.fetchall()
    #     cursor.close()
    #     return self.cx_info


# data_manager = DataManager()
# response = data_manager.get_dest_info()
# print(response)