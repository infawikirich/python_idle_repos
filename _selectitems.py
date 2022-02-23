# the view the database
import sqlite3

# create a connection
con = sqlite3.connect("COMPANY.db")

# create a cursor
cur = con.cursor()


# low to view the data
for row in cur.execute("SELECT * FROM COMPANY ORDER BY AGE"):
    print(row)


con.close()
