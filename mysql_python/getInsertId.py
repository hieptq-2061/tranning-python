import connect

try:
    mycursor = connect.mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Michelle", "Blue Village")
    mycursor.execute(sql, val)

    connect.mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)
except Exception as e:
    print(e)
