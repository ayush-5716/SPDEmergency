import mysql.connector
import hashlib
import datetime

db = mysql.connector.connect(host="localhost", username="root", password="sqlsme", database="library")
cr = db.cursor()

def library_status():
    return 8 < datetime.datetime.now().hour < 20


def time_right_now():
    return datetime.datetime.now().strftime("%X")

def login_check(username, password):
    cr.execute()
db.close()