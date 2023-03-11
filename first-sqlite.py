import sqlite3

con = sqlite3.connect('customer.db')

#create a cursor
c = con.cursor()

#create a table
#c.execute("""CREATE TABLE customers (
  #  firstName text,
   # lastName text,
    #email text
    
#)""")

"""many_customers  = [

        ('law', 'omodi', 'omondi@gmail.com'), 
        ('cren', 'conso', 'conso@gmail.com'), 
        ('chris', 'achinga', 'achiga@gmail.com')
        ]
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)"""

c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()

for item in items:
    print(item)


con.commit()
con.close()
