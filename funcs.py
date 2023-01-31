import mysql.connector
import hashlib
import datetime

db = mysql.connector.connect(host="localhost", username="root", password="sqlsme", database="library")
cr = db.cursor()

def library_status():
    return 8 < datetime.datetime.now().hour < 20



db.close()