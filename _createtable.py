# create a table for the database
import sqlite3

# create a connection
con = sqlite3.connect('COMPANY.db')


# creat a cursor
cur = con.cursor()

# add items to the database
cur.execute(""" CREATE TABLE DEPARTMENT 
                (ID INT PRIMARY KEY NOT NULL,
                 DEPT CHAR(50) NOT NULL,
                 EMP_ID INT NOT NULL)
            """)
# commint
con.commit()


#close the connectioin
con.close()

               
