import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Virendar&4'
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE!")