#Name: Maxwell Singer
#NetID: mss556
#Class: Methods and Tools in SW Dev
#
#User class file

import mysql.connector
import sys

class User:

    # Initialization
    def __init__(self, userID=00000, password="00000", name="00000",
                 billingAddress="00000", shippingAddress="00000",
                 paymentMethod="00000", cartId=00000):
        self.userID = userID
        self.password = password
        self.name = name
        self.billingAddress = billingAddress
        self.shippingAddress = shippingAddress
        self.paymentMethod = paymentMethod
        self.cartId = cartId

    # Sign in
    def signUp(self, userID, password):

        #Check to see if connection can be established
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="FinalProject")
        except:
            print("Failed connect.")

            sys.exit()

        # Set cursor
        cursor = connection.cursor()

        # Attempt an insert of the new userID and password
        # Integrity Error will throw if the userID is already present
        # Account for that, and have a final except for any other errors.
        try:
            query = "INSERT INTO `Users`(`UserID`, `CartID`, `Password`, `Name`, `Billing Address`, `Shipping Address`, `Payment Method`) VALUES ('{}','1','{}','','','','');"

            query = query.format(userID, password)

            cursor.execute(query)

        # Except for userID already present
        except mysql.connector.errors.IntegrityError:
            print("There is already an account with this userID.")

            
        except:
            print("An error occurred, please try again.")


        # Commit insert, close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()


    # Login  
    def login(self):

        # Basic login menu
        print("Login:")
        userID = input("UserID: ")
        password = input("Password: ")

        # Check to see if connection can be established
        # If not, exit
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="FinalProject")
            
        except:
            print("Failed connect.")

            sys.exit()

        # Set cursor
        cursor = connection.cursor()

        # Set query, format where appropriate with userID and password
        query = "SELECT `UserID`, `Password` FROM `Users` WHERE UserID='{}' AND Password='{}'"
        query = query.format(userID, password)

        # Execute query, fetchall, store in login submission
        cursor.execute(query)
        login_submit = cursor.fetchall()

        # If result isn't empty (Meaning there was a valid
        # userID-password pair found), select contents of
        # user and populate the class values.
        # Else, tell user either input was not valid, exit.
        if len(login_submit) > 0:
            
            print("Account found. Loading account info.")
            print()

            # Set query and format with appropriate userID
            query = "SELECT * FROM `Users` WHERE UserID='{}'"
            query = query.format(userID)

            # Execute query, fetchall, store in user info
            cursor.execute(query)
            user_info = cursor.fetchall()

            # Set user information to user class
            self.userID = user_info[0][0]
            self.set_name(user_info[0][3])
            self.set_billingAddress(user_info[0][4])
            self.set_shippingAddress(user_info[0][5])
            self.set_payment(user_info[0][6])

            
        else:
            print("Invalid userID or password, try again.")
            sys.exit()

        # Print user info
        # (Can be removed later, ie after menuing)
        self.print_info()

        # Close cursor and connection
        cursor.close()
        connection.close()

        

    #getters
    def get_userID(self):
        return self.userID

    def get_name(self):
        return self.name

    def get_billingAddress(self):
        return self.billingAddress

    def get_shippingAddress(self):
        return self.shippingAddress

    def get_payment(self):
        return self.paymentMethod

    #setters
    def set_name(self, name):
        self.name = name

    def set_billingAddress(self, addr):
        self.billingAddress = addr

    def set_shippingAddress(self, addr):
        self.shippingAddress = addr

    def set_payment(self, payment):
        self.paymentMethod = payment

    #print statement
    def print_info(self):
        print("Account information: ")
        print("User ID:", self.get_userID())
        print("Name:", self.get_name())
        print("Billing Address:", self.get_billingAddress())
        print("Shipping Address:", self.get_shippingAddress())
        print("Payment Method:", self.get_payment())




def main():

    generic = User()

    generic.login()

if __name__ == '__main__':
    main()




    
