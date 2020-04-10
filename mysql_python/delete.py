import connect

try:
    mycursor = connect.mydb.cursor()
    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

    mycursor.execute(sql)

    connect.mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
except Exception as e:
    print(e)
