import sqlite3

# first of all you need to connect to the database

conn_db = sqlite3.connect('customer.db')

# create a cursor object with with we will use to invoke method to
# manipulate the sqlite

c = conn_db.cursor()

#query the database
c.execute("SELECT * FROM customers WHERE lastName = 'Awanzi'")

items = c.fetchall()
for item in items:
    print(item)

# commit our command
conn_db.commit()

# close our connection
conn_db.close()
