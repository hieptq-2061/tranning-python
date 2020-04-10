import connect

try:
    mycursor = connect.mydb.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS customers
        (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255)
        )""")
    print('create table success')
except Exception:
    print('exception')
