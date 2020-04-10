import connect

try:
    mycursor = connect.mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
except Exception as e:
    print(e)
