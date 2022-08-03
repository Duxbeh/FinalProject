import mysql.connector
import sys


class Cart:
    @staticmethod
    def add_item(itemID, qty):
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
        i = 1
        cursor = connection.cursor()

        query = ("INSERT INTO cart (ID, name, price, qty) SELECT ID, name, price, %d From inventory Where ID = %d" % (
            qty, itemID))

        cursor.execute(query)
        connection.commit()

        print(cursor.rowcount, "record(s) inserted.")

        cursor.close()
        connection.close()
        print()
        print()

    @staticmethod
    def remove_item(itemID):
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
        cursor = connection.cursor()

        query = ("DELETE FROM cart WHERE ID=%d" % itemID)

        cursor.execute(query)

        connection.commit()

        print(cursor.rowcount, "record deleted.")
        print()
        cursor.close()
        connection.close()

    @staticmethod
    def display_cart():
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
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cart")

        result = cursor.fetchall()
        for x in result:
            print("Name", x[1])
            print("ID: ", x[0], "\tPrice:", x[2], "\tQty:", x[3])
            print()
            cursor.close()
            connection.close()


class Inventory:
    @staticmethod
    def display_inventory():
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
        cursor = connection.cursor()

        query = "UPDATE Inventory SET Stock=%d WHERE ID=%d"

        cursor.execute(query, quantity, itemID)

        connection.commit()

        cursor.close()
        connection.close()


def main():
    status = True
    inv = Inventory()
    cart = Cart()
    while status:
        print("1. display inventory")
        print("2. add item to shopping cart")
        print("3. remove item from shopping cart")
        print("4. display shopping cart")
        print("5. Check out")
        print("6. exit")

        user_in = int(input("Enter your choice: "))
        if user_in == 1:
            inv.display_inventory()
        elif user_in == 2:
            itemID = int(input("Enter item ID number: "))
            qty = int(input("Enter quantity of the item: "))

            cart.add_item(itemID, qty)
            # inv.update_item(itemID, qty)

        elif user_in == 3:
            itemID = int(input("Enter item ID number: "))
            cart.remove_item(itemID)

        elif user_in == 4:
            cart.display_cart()

        elif user_in == 6:
            status = False

        else:
            print("Invalid selection\n")


if __name__ == '__main__':
    main()
