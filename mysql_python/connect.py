import mysql.connector

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="mydatabase"
    )
except Exception:
    print('connect database fail')
