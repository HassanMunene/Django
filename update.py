import sqlite3

# make a connection
conn_db = sqlite3.Connection('customer.db')

# create an instance of a cursor so as to invoke methods
c = conn_db.cursor()

# update records
c.execute("""UPDATE customers SET firstName = 'Awanzi'
        WHERE rowid = 1
        """)

# commit the changed
conn_db.commit()

c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()

for item in items:
    print(item)

# close the connection
conn_db.close()
