import mysql.connector

def create_connection ():
    connection = mysql.connector.connect(
        host='localhost',
        password = '**********',
        user='root',
        database = 'EmployeeManagement')

    return connection

def close_connection(connection):
    if connection.is_connected():
        connection.close()
    else :
        print('Not Connected ')

def Add_Employee (connection, employee_id, name, age, department, salary):
    cursor = connection.cursor()
    query = "INSERT INTO Employee (EmployeeID, Name, Age, Department, Salary) VALUES (%s, %s, %s, %s, %s)"
    data = (employee_id, name, age, department, salary)
    cursor.execute(query, data)
    connection.commit()

def View_Employee_Data (connection):
    cursor = connection.cursor()
    Query = ("SELECT * FROM Employee")
    cursor.execute(Query)
    rows = cursor.fetchall()
    for giveData in rows :
        print(giveData)

def update_employee_data(connection, employee_id, name, age, department, salary):
    cursor = connection.cursor()
    query = """
        UPDATE Employee
        SET Name = %s, Age = %s, Department = %s, Salary = %s
        WHERE EmployeeID = %s
    """
    data = (name, age, department, salary, employee_id)
    cursor.execute(query, data)
    connection.commit()
    
def Delete_Employee_Data (connection,EmployeeID):
    cursor = connection.cursor()
    Query = ("DELETE FROM Employee WHERE EmployeeID = %s ")
    cursor.execute(Query, (EmployeeID,))
    connection.commit()

def Main_Function ():
    connection = create_connection()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Adding The Employee Data ...")
            EmployeeID = int(input("Enter The ID Of The Employee : "))
            Name = input("Enter The Name Of The Employee : ")
            Age = int(input("Enter The Age Of The Employee : "))
            Department = input("Enter The Department Of The Employee : ")
            Salary = int(input("Enter The Salary Of The Emlpoyee: "))

            Add_Employee(connection,EmployeeID,Name,Age,Department,Salary)

        elif choice == 2:
            print("Viewing The Employee Data ...")
            View_Employee_Data(connection)

        elif choice == 3:
            print("Updating The Employee Data ...")
            employee_id = int(input("Enter The ID Of The Employee: "))
            name = input("Enter The Name Of The Employee: ")
            age = int(input("Enter The Age Of The Employee: "))
            department = input("Enter The Department Of The Employee: ")
            salary = float(input("Enter The Salary Of The Employee: "))
            update_employee_data(connection, employee_id, name, age, department, salary)

        elif choice == 4 :
            print("Deleting The Employee Data ...")
            Employee_Id = int(input("Enter The ID Of The Employee  : "))
            Delete_Employee_Data(connection,Employee_Id)

        elif choice == 5:
            print("QUITING THE PROGRAM ...")
            break
        
        else:
            print("Invalid choice. Please try again.")

    close_connection(connection)

password = "123Azamil"
Enter = input("Enter The Password : ")

if Enter == password:
    Main_Function()

else:
    print("Wrong Password , Please Try Again !!..")
