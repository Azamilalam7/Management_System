import mysql.connector

def create_connection ():
    connection = mysql.connector.connect(
        host='localhost',
        password = '**********',
        user='root',
        database = 'Cafe_Management')

    return connection

def close_connection(connection):
    if connection.is_connected():
        connection.close()
    else :
        print('Not Connected ')

class Cafe :
    def __init__ (self):
        print("****** Cafe Management System ******")
        print("****** Created By Azamil Alam ******")
    @staticmethod
    def Add_Cafe_Data (connection, customer_id, customer_name, order_name, order_date, order_price):
        cursor = connection.cursor()
        query = "INSERT INTO Cafe (Customer_ID, Customer_Name, Order_Name, Order_Date, Order_Price) VALUES (%s, %s, %s, %s, %s)"
        data = (customer_id, customer_name, order_name, order_date, order_price)
        cursor.execute(query, data)
        connection.commit()
    @staticmethod
    def View_Cafe_Data (connection):
        cursor = connection.cursor()
        query = "SELECT * FROM Cafe "
        cursor.execute(query)
        row = cursor.fetchall()
        for rows in row :
            print(rows)
    @staticmethod
    def Update_Cafe_Data (connection, customer_id, customer_name, order_name, order_date, order_price):
        cursor = connection.cursor()
        query = """
                    UPDATE Cafe
                    SET Customer_Name = %s, Order_Name = %s, Order_Date = %s, Order_Price = %s
                    WHERE Customer_ID = %s
                """
        data = (customer_name, order_name, order_date, order_price, customer_id)
        cursor.execute(query, data)
        connection.commit()
    @staticmethod
    def Delete_Cafe_Data (connection,Customer_ID):
        cursor = connection.cursor()
        query = "DELETE FROM Cafe WHERE Customer_ID = %s"
        cursor.execute(query, (Customer_ID,))
        connection.commit()

Manager = Cafe ()

def Main_Function ():
    connection = create_connection()

    while True:
        print("\nCafe Management System")
        print("1. Add Order")
        print("2. View All Orders")
        print("3. Update Order")
        print("4. Delete Order")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            
            customer_id = int(input("Enter The ID Of The Customer: "))
            customer_name = input("Enter The Name Of The Customer: ")
            order_name = input("Enter The Name Of The Order: ")
            order_date = input("Enter The Date Of The Order (YYYY-MM-DD): ")
            order_price = float(input("Enter The Price Of The Order: "))
            Cafe.Add_Cafe_Data(connection, customer_id, customer_name, order_name, order_date, order_price)
            print("Adding The Order Data ...")

        elif choice == 2:
            print("Viewing The Data : ")
            Cafe.View_Cafe_Data(connection,)

        elif choice == 3:
            customer_id = int(input("Enter The ID Of The Customer: "))
            customer_name = input("Enter The Name Of The Customer: ")
            order_name = input("Enter The Name Of The Order: ")
            order_date = input("Enter The Date Of The Order (YYYY-MM-DD): ")
            order_price = float(input("Enter The Price Of The Order: "))
            Cafe.Update_Cafe_Data(connection, customer_id, customer_name, order_name, order_date, order_price)
            print("Updating The Order Data ...")

        elif choice == 4:
            customer_id = int(input("Enter The ID Of The Customer: "))
            Cafe.Delete_Cafe_Data(connection,customer_id)
            print("Deleting The Cafe Data")

        elif choice == 5:
            print("QUITING THE PROGRAM !.!.")
            break
        else :
            print("InValid Choice ! Please Try gain !!! ")

    close_connection(connection)

# Authtication

password = "123!@#"
Enter = input("Input The Password To Enter In  Cafe Management System  : ")
if Enter == password :
    Main_Function()