import connect

try:
    mycursor = connect.mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    connect.mydb.commit()

    print(mycursor.rowcount, "record inserted.")
except Exception as e:
    print(e)
