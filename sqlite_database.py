# improt sqlite3 module
import sqlite3

# use the try exception to catch any error
try:
    # create a connect to the detabase
    con = sqlite3.connect('Tutorial_DB.db')

    # create a cursor to the connection
    cur = con.cursor()

    # createa query to the table
    create_table = (""" CREATE TABLE TUTORIAL_CLASS
                        (ID INT PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        EMAIL TEXT NOT NULL UNIQUE,
                         JOINING_DATE DATETIME,
                         SALARY REAL NOT NULL);
                    """)

    # execute the query
    cur.execute(create_table)

    # commit to the database for the changes
    con.commit()

    # close the cursor
    cur.close()

except sqlite3.Error as error:
    print('Error while creating a sqlite table', error)

finally:
    if con:
        con.close()
        print('sqlite connection is closed successfully')
