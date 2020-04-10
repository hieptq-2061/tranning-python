import connect

try:
    mycursor = connect.mydb.cursor()
    sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
except Exception as e:
    print(e)
