import sqlite3

conn = sqlite3.connect("DB.db")
cursor = conn.cursor()

def SelectService():
    data = cursor.execute("SELECT * FROM Service")
    return data