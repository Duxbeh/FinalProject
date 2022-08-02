import mysql.connector
import sys


try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="methods"
    )

    print("Successful connection.\n")

except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()


class Inventory:
    @staticmethod
    def display_inventory():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Inventory")

        result = cursor.fetchall()

        for x in result:
            print("ID:", x[0], "\tName:", x[1])
            print("Platform:", x[2], "\tPrice:", x[3], "\tStock:", x[4])
            print()
        cursor.close()
        connection.close()

    @staticmethod
    def update_item(itemID, quantity):
        cursor = connection.cursor()

        query = "UPDATE Inventory SET Stock=%d WHERE ID=%d"

        cursor.execute(query, quantity, itemID)

        connection.commit()

def main():
    status = True
    inv = Inventory
    while status:
        print("1. display inventory")
        print("2. exit")

        user_in = int(input("Enter your choice: "))
        if user_in == 1:
            inv.display_inventory()
        elif user_in == 2:
            status = False
        else:
            print("Invalid selection\n")

if __name__ == '__main__':
    main()
