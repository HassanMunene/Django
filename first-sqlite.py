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

c.execute("SELECT * FROM customers")
print(c.fetchmany(3))


con.commit()
con.close()
