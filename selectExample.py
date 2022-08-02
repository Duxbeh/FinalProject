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

print()  ## spacing's sake

## cursor to send queries through
cursor = connection.cursor()

## sends query and grabs data
## SELECT queries return a tuple for each row contained in a list
## --> a list of tuples
cursor.execute("SELECT * FROM books")

## only needed if you're running a SELECT
## this actually grabs the data
result = cursor.fetchall()

## illustrates what unformatted results look like
print("Enter result set: ", result, sep="\n", end="\n\n\n")

for x in result:
    ## you can print the entire tuple --> print(x)
    ## or you can print items from it using indices
    ## first item --> x[0]
    ## second item --> x[1]
    ## etc... (for however many columns a result has)

    print("Entire row:", x, "\n")  ## all

    print("Row broken down into each column: ")
    for y in x:
        print(y)
    print()

    print("ISBN:", x[0])  ## only the ISBN
    print("Title:", x[1], "\tAuthor:", x[2])
    print("\n\n")

## a few more examples ...

## selecting specific columns
## goal: shows how column order affects tuple order
print("Specific column select: ")

cursor.execute("SELECT Title, Author FROM books")
result = cursor.fetchall()

## because of the SELECT query
## 0 --> Title
## 1 --> Author
## if not selecting ALL columns, numbering is based on query order
for x in result:
    print(x[0], "by", x[1])

## selecting a specific column of a specific row
## goal: shows how it'd work even if you're only selecting one specific item
## even though you're only grabbing on item, it's still in a list of tuples
print("\n\n\nSpecific column/row select:")

cursor.execute("SELECT Title FROM books WHERE ISBN='978-0307265432'")
result = cursor.fetchall()

print("Unformatted result:", result)

title = result[0][0]  ## grabs the single item
print("Title you grabbed:", title)

## close the cursor and connection once you're done
cursor.close()
connection.close()
