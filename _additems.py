# create a table for the database
import sqlite3

# create a connection
con = sqlite3.connect('COMPANY.db')


# creat a cursor
cur = con.cursor()

# add items to the database
cur.execute(""" INSERT INTO COMPANY
            VALUES (1, 'Paul', 32, 'California', 20000.00)
            """)

cur.execute(""" INSERT INTO COMPANY
            VALUES (3, 'Teddy', 23, 'Norway', 20000.00)
            """)

cur.execute(""" INSERT INTO COMPANY
            VALUES (4, 'Mark', 25, 'Rich-mond', 65000.00)
            """)

cur.execute(""" INSERT INTO COMPANY
            VALUES (5, 'David', 27, 'Texas', 85000.00)
            """)

cur.execute(""" INSERT INTO COMPANY
            VALUES (6, 'Kim', 22, 'South-Hall', 45000.00)
            """)

# commint
con.commit()


#close the connectioin
con.close()

                 
