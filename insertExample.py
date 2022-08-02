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
cursor.execute("INSERT INTO books (ISBN, Title, Author, Year, Genre) VALUES ('987-0441172719', 'Dune', 'Frank Herbert', '1965', 'Science Fiction')")

## commits to database
## **needed** for changes to be made to a table
connection.commit()

## shows changes
print(cursor.rowcount, "record inserted.")
print()


## example 2

## makes a string for the query and a tuple for the data
## %s --> allows Python to substitute a value
query = "INSERT INTO books (ISBN, Title, Author, Year, Genre) VALUES (%s, %s, %s, %s, %s)"
data = ("978-0593244036", "Wuthering Heights", "Emily Bronte", "1847", "Gothic Literature")

## sends query and data
cursor.execute(query, data)

## commits change
connection.commit()

## shows changes
print(cursor.rowcount, "record inserted.")
print()


## example 3

## creates a query to make multiple rows at once
## creates a list of multiple tuples where each tuple is a row to be insert
query = "INSERT INTO books (ISBN, Title, Author, Year, Genre) VALUES (%s, %s, %s, %s, %s)"
data = [
    ("978-1451673319", "Fahrenheit 451", "Ray Bradbury", "1953", "Dystopian Fiction"), # row 1
    ("978-1435146914", "The Divine Comedy", "Dante Alighieri", "1320", "Narrative Poem"), # row 2
]

## sends query and data
## notice: execute line has changed!
cursor.executemany(query, data)

## commits change
connection.commit()

## shows changes
print(cursor.rowcount, "record(s) inserted.")


## close the cursor and connection once you're done
cursor.close()
connection.close()
