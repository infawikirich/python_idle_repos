# the view the database
import sqlite3

# create a connection
con = sqlite3.connect("COMPANY.db")

# create a cursor
cur = con.cursor()

# drop one of the table
cur.execute("UPDATE COMPANY set ADDRESS = 'Texas' where ID = 2")

con.commit()

con.close()
