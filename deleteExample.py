import mysql.connector
import sys

## attempts to connect to the database
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="methods"
    )

    print("Successful connection.")

except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

## cursor to send queries through
cursor = connection.cursor()


## example 1

## sends query
cursor.execute("DELETE FROM books WHERE Title='Dune'")

## commits to database
## **needed** for changes to be made to a table
connection.commit()

## shows changes
print(cursor.rowcount, "record deleted.")
print()


## example 2

## makes a string for the query and a tuple for the data
## %s --> allows Python to substitute a value
query = "DELETE FROM books WHERE Title=%s"

## deleting --> weird quirk where you need to have a second blank item
## so the tuple has ", " at the end of it, no matter how many items used
data = ("Wuthering Heights",)

## sends query and data
cursor.execute(query, data)

## commits change
connection.commit()

## shows changes
print(cursor.rowcount, "record deleted.")
print()


## example 3

## creates a query to delete multiple rows at once
## creates a list of multiple tuples where each tuple is a row to be deleted
query = "DELETE FROM books WHERE Title=%s"
data = [
    ("Fahrenheit 451", ), # row 1
    ("The Divine Comedy", ), # row 2
]

## sends query and data
## notice: execute line has changed!
cursor.executemany(query, data)

## commits change
connection.commit()

## shows changes
print(cursor.rowcount, "record(s) deleted.")


## close the cursor and connection once you're done
cursor.close()
connection.close()
