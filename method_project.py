import mysql.connector
import sys
import time




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
        # number is primary key so it can not repeat this try block will insert the first item, if number is repeated it
        # will raise error
        try:

            i = 1
            cursor = connection.cursor()

            query = ( "INSERT INTO cart (number, ID, name, price, qty) SELECT %d, ID, name, price, %d From inventory Where "
                        "ID = %d" % (i, qty, itemID))

            cursor.execute(query)
            connection.commit()
            print()
            print("\nItem(s) added\n")

            cursor.close()
            connection.close()
            print()
            print()
        # if error raise means number is repeated, so this block will increment the last number by one and insert the
        # item
        except:
            cursor = connection.cursor()
            cursor.execute("SELECT number FROM cart")
            result = cursor.fetchall()
            list = []
            for x in result:
                list.append(x[0])
            list.sort()
            list.reverse()
            num = list[0] + 1
            query = ("INSERT INTO cart (number, ID, name, price, qty) SELECT %d, ID, name, price, %d From inventory Where "
                        "ID = %d" % (num, qty, itemID))

            print()
            print("\nItem(s) added\n")
            print()
            print()

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

        # this function will check if the item is already exit, if yes, then it will update the qty of that item,
        # so it will not generate a duplicate row
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
            print()
            print("\nItem(s) added\n")
            connection.commit()

            cursor.close()
            connection.close()

    @staticmethod
    def remove_item(itemID, qty):
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

        cursor.execute("SELECT qty FROM cart where ID=%d" % itemID)
        result = cursor.fetchall()
        List = []
        for x in result:
            List.append(x[0])

        qty_before = List[0]
        if qty == qty_before:
            query = ("DELETE FROM cart WHERE ID=%d" % itemID)
            cursor.execute(query)

            connection.commit()
            print()
            print("Item(s) removed")
            print()
            cursor.close()
            connection.close()
        else:
            qty_after = qty_before - qty
            query = ("UPDATE cart SET qty=%d WHERE ID=%d" % (qty_after, itemID))
            cursor.execute(query)

            connection.commit()
            print()
            print("Item(s) removed")
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

            # exits the program if unsuccessful
            sys.exit()

        # remove all the item in the cart and display user a subtotal
        cursor = connection.cursor()
        cursor.execute("SELECT price, qty FROM cart")
        result = cursor.fetchall()

        list = []
        for x in result:
            list.append(float(x[0]) * float(x[1]))
        total = sum(list)
        print("Subtotal:$%.2f" % total)
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
    # this function will update the inventory after item been added to the cart
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
    # this function will update the inventory after item been removed from the cart
    def update_item_remove(itemID, qty):
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

        stock_after = stock + qty

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
            try:
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="methods"
                    )
                except:
                    print("Failed connection.")
                    sys.exit()

                itemID = int(input("Enter item ID number: "))
                qty = int(input("Enter quantity of the item: "))

                cursor = connection.cursor()
                cursor.execute("SELECT Stock FROM inventory where ID=%d" % itemID)
                result = cursor.fetchall()
                for x in result:
                    actual_stock = int(x[0])

                if qty < 0 or qty > actual_stock:
                    raise Exception("Invalid input for quantity!")
                else:
                    try:
                        cart.check_duplicate(itemID, qty)
                        inv.update_item_add(itemID, qty)
                        print()
                        print()
                    except:
                        cart.add_item(itemID, qty)
                        inv.update_item_add(itemID, qty)
            except:
                print("\ninvalid input\n")
                print('\n')

        elif user_in == 3:
            try:
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="methods"
                    )
                except:
                    print("Failed connection.")
                    sys.exit()

                itemID = int(input("Enter item ID number: "))
                qty = int(input("Enter quantity to remove: "))

                cursor = connection.cursor()
                cursor.execute("SELECT qty FROM cart where ID=%d" % itemID)
                result = cursor.fetchall()
                for x in result:
                    actual_qty = int(x[0])
                if qty < 0 or qty > actual_qty:
                    raise Exception("Invalid input for quantity!")
                else:
                    cart.remove_item(itemID, qty)
                    inv.update_item_remove(itemID, qty)
            except:
                print("\ninvalid input\n")
                print('\n')
        elif user_in == 4:
            cart.display_cart()

        elif user_in == 5:
            cart.checkout()

        elif user_in == 6:
            status = False

        else:
            print("\nInvalid selection\n")


if __name__ == '__main__':
    main()
