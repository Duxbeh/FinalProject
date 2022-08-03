import mysql.connector
import sys
import time

i = 0

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

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
            sys.exit()

        try:
            global i
            i += 1
            cursor = connection.cursor()

            query = ("INSERT INTO cart (number, ID, name, price, qty) SELECT %d, ID, name, price, %d From inventory Where "
                     "ID = %d" % (i, qty, itemID))

            cursor.execute(query)
            connection.commit()

            print(cursor.rowcount, "record(s) inserted.")

            cursor.close()
            connection.close()
            print()
            print()
        except:
            cursor = connection.cursor()
            cursor.execute("SELECT number FROM cart")
            result = cursor.fetchall()
            list = []
            for x in result:
                list.append(x[0])

            list.reverse()
            i = list[0] + 1

            query = ("INSERT INTO cart (number, ID, name, price, qty) SELECT %d, ID, name, price, %d From inventory Where "
                        "ID = %d" % (i, qty, itemID))

            print(cursor.rowcount, "record(s) inserted.")

            cursor.execute(query)
            connection.commit()

            cursor.close()
            connection.close()

    @staticmethod
    def check_duplicate(itemID, qty):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="methods"
            )

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
            sys.exit()

        cursor = connection.cursor()
        cursor.execute("SELECT ID FROM cart where ID=%d" % itemID)
        result1 = cursor.fetchall()
        for j in result1:
            cmp = j[0]

        if cmp == itemID:
            list = []
            cursor.execute("SELECT qty FROM cart where ID=%d" % itemID)
            result2 = cursor.fetchall()
            for x in result2:
                list.append(x[0])
            qty_after = list[0] + qty
            query = ("UPDATE cart SET qty=%d WHERE ID=%d" % (qty_after, itemID))
            cursor.execute(query)

            connection.commit()

            cursor.close()
            connection.close()



    @staticmethod
    def remove_item(itemID):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="methods"
            )

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
            print()
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cart")

        result = cursor.fetchall()
        for x in result:
            print("Name", x[2])
            print("ID: ", x[1], "\tPrice:", x[3], "\tQty:", x[4])
            print()
            cursor.close()
            connection.close()

    @staticmethod
    def checkout():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="methods"
            )

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
            sys.exit()

        cursor = connection.cursor()
        cursor.execute("SELECT price FROM cart")
        result = cursor.fetchall()

        list = []
        for x in result:
            list.append(x[0])
        total = sum(list)
        print("Subtotal:$%d" % total)
        time.sleep(3)
        print("Thanks for your order")
        print()

        cursor.execute("DELETE FROM cart")
        connection.commit()
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
            print()

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
    def update_item_add(itemID, qty):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="methods"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        cursor.execute("SELECT Stock FROM inventory where ID=%d" % itemID)
        result = cursor.fetchall()
        for x in result:
            stock = int(x[0])

        stock_after = stock - qty

        query = ("UPDATE Inventory SET Stock=%d WHERE ID=%d" % (stock_after, itemID))

        cursor.execute(query)

        connection.commit()

        cursor.close()
        connection.close()

    @staticmethod
    def update_item_remove(itemID):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="methods"
            )
        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()

        list = []
        cursor.execute("SELECT qty FROM cart where ID=%d" % itemID)
        result = cursor.fetchall()
        for x in result:
            list.append(x[0])

        cursor.execute("SELECT Stock FROM inventory where ID=%d" % itemID)
        result2 = cursor.fetchall()
        for i in result2:
            list.append(i[0])

        stock_after = sum(list)

        query = ("UPDATE Inventory SET Stock=%d WHERE ID=%d" % (stock_after, itemID))

        cursor.execute(query)

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
            try:
                cart.check_duplicate(itemID, qty)
                inv.update_item_add(itemID, qty)
            except:
                cart.add_item(itemID, qty)
                inv.update_item_add(itemID, qty)

        elif user_in == 3:
            itemID = int(input("Enter item ID number: "))
            inv.update_item_remove(itemID)
            cart.remove_item(itemID)

        elif user_in == 4:
            cart.display_cart()

        elif user_in == 5:
            cart.checkout()

        elif user_in == 6:
            status = False

        else:
            print("Invalid selection\n")


if __name__ == '__main__':
    main()
