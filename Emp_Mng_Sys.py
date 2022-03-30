#_________________________________EMPLOYEE_MANAGEMENT_SYSTEM_____________________________________#
import mysql.connector

# CONNECTING MYSQL WITH PYTHON

mydb=mysql.connector.connect(host='localhost', user='root', password='Situ321@#', database="EMP_Management_SYS")
myacces=mydb.cursor()

# myacces.execute("CREATE DATABASE EMP_Management_SYS")

# myacces.execute("CREATE TABLE Employee_TABLE (Employee_ID int not null, name varchar (30) not null, address varchar (30) not null, DOB varchar (30) not null, contact_no varchar (30) not null);")
# sql="INSERT INTO Employee_TABLE (Employee_ID, name, address, DOB, contact_no ) VALUES(%s,%s,%s,%s,%s)"

#                           CREATED TABLE AND INSERTING VALUES      

# val=[(105, "Preeti","Dehradun", "01/04/1999", 9934000012),
#     (106, "Sapna", "Delhi", "21/05/2000", 4490120923),
#     (107, "Ashna","Gurugram" , "10/09/1998", 8423003083),
#     (108, "Sheetal","Chandigarh" ,"10/07/2000", 9012120411)]

# myacces.executemany(sql, val)
# mydb.commit()


#_________________________________________CHECKING EMPLOYEE_________________________________________#
#                       THIS FUNCTIONS RETURNS TRUE IF THE EMP_ID EXIST ELSE FALSE

def checking_employee_Id(Employee_id):
 
    # Query to select all Rows from table
    check = 'SELECT * from Employee_TABLE where Employee_ID=%s'
 
    # making cursor buffered to make rowcount method work properly
    my_access = mydb.cursor(buffered=True)
    data = (Employee_id,)
 
    # Executing the SQL Query
    my_access.execute(check, data)
 
    # rowcount method to find
    # number of rows with given values
    result = my_access.rowcount
    if result == 1:
        return True
    else:
        return False


#_________________________________________ADDING A NEW EMPLOYEE__________________________________________#
 

def Input_details():
    Emp_Id = int(input("Enter Employee Id : "))
    if(checking_employee_Id(Emp_Id) == True):
        print("Employee with this id aready exists\n")
        main_function()
    else:
        Name = input("Enter Employee Name : ")
        address = input("Enter Employee address : ")
        D_O_B = input("Enter Employee date of birth : ")
        contact = input("Enter Employee contact number : ")
        data=  (Emp_Id, Name, address, D_O_B, contact)
 
        # Inserting Employee details in the Employee Table
        sql = 'INSERT INTO Employee_TABLE values(%s,%s,%s,%s,%s)'
        c = mydb.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in the table
        mydb.commit()
        print("Employee Added Successfully ")
        main_function()


#_______________________________________DISPLAY EMPLOYEE__________________________________________#
#                              To show all the Employees detials

def Get_Info():
    sql = 'SELECT * from Employee_TABLE'
    my_acc = mydb.cursor()           
    my_acc.execute(sql)
    # Fetching all details of all the Employees
    result = my_acc.fetchall()
    c=1
    for i in result:
        print("EMLOYEE ", c) 
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee adress : ", i[2])
        print("Employee Salary : ", i[3])
        print("Employee contact No. ", i[4])
        print("                                                                                        ")
        print("-------------------------------------------------------------------------------------")
        print("                                                                                        #  ")
        c+=1
    main_function()

#___________________________SEARCH FOR A PARTICULAR EMPLOYEE DETAILS__________________________________#

def Search_employee():
    Id = int(input("Enter Employee Id for the employee details: "))

    if(checking_employee_Id(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        main_function()
    else:
        myacces.execute("""SELECT Employee_ID, name, address, DOB, contact_no FROM Employee_TABLE WHERE Employee_ID = %s""", (Id,))
        for row in iter(myacces.fetchone, None):
            print( )
            print("Employee Id : ", row[0])
            print("Employee Name : ", row[1])
            print("Employee adress : ", row[2])
            print("Employee Salary : ", row[3])
            print("Employee contact No. ", row[4])
        main_function()

#__________________________________________UPDATE EMPLOYEE DETAILS_________________________________________#

def Update_employee():
    Id = int(input("Enter Employee Id : "))

    if(checking_employee_Id(Id) == False):
        print("Employee does not  exists\n")
        main_function()
    else:
        print(" pick 1 to update Employee Name")
        print(" pick 2 to update Employee address")
        print(" pick 3 to update Employee Date of birth")
        print(" pick 4 to update Employee Mobile No.")
        select_col_name=int(input("enter column name to update: "))

        if select_col_name==1:
            Next_Emp_Name=input("enter a Another name: ")
            sql = 'SELECT name from Employee_TABLE where Employee_ID=%s'
            data = (Id,)
            c = mydb.cursor()
            c.execute(sql, data)          
            r = c.fetchone()
            # Query to Update NAME of Employee with Previous name
            sql = 'UPDATE Employee_TABLE set name=%s where Employee_ID=%s'
            d = (Next_Emp_Name, Id)
            c.execute(sql, d)
            mydb.commit()
            print("Employee Name changed successfully")
            main_function()

        elif select_col_name==2:
            Next_Emp_Address=input("enter a Another Address: ")
            sql = 'SELECT address from Employee_TABLE where address=%s'
            data = (Id,)
            c = mydb.cursor()
            c.execute(sql, data)
            r = c.fetchone()
            sql = 'UPDATE Employee_TABLE set address=%s where Employee_ID=%s'
            d = (Next_Emp_Address, Id)
            c.execute(sql, d)
            mydb.commit()
            print("Employee address changed successfully")
            main_function()

        elif select_col_name==3:
            Next_Emp_DOB=input("enter a Another Date Of Birth: ")
            sql = 'SELECT DOB from Employee_TABLE where Employee_ID=%s'
            data = (Id,)
            c = mydb.cursor()
            c.execute(sql, data)
            r = c.fetchone()
            sql = 'UPDATE Employee_TABLE set DOB=%s where Employee_ID=%s'
            d = (Next_Emp_DOB, Id)
            c.execute(sql, d)
            mydb.commit()
            print("Employee Date of Birth changed successfully")
            main_function()

        elif select_col_name==4:
            Next_Emp_contact_NO=input("enter a Another Contact_no: ")
            sql = 'SELECT contact_no from Employee_TABLE where Employee_ID=%s'
            data = (Id,)
            c = mydb.cursor()
            c.execute(sql, data)
            r = c.fetchone()
            sql = 'UPDATE Employee_TABLE set contact_no=%s where Employee_ID=%s'
            d = (Next_Emp_contact_NO, Id)
            c.execute(sql, d)
            mydb.commit()
            print("Employee contact no. changed successfully")
            main_function()
        

#_____________________________________REMOVE EMPLOYEE Details_________________________________________#

def Remove_Employ():
    Id = int(input("Enter Employee Id : "))
    if(checking_employee_Id(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        main_function()
    else:
        sql = 'DELETE FROM Employee_TABLE WHERE Employee_ID=%s'
        data = (Id,)
        c = mydb.cursor()
        c.execute(sql, data)
        mydb.commit()
        print("Employee Removed")
        main_function()

#___________________________________________Main_Function_________________________________________#


def main_function():
    print("                                                                                                 ")
    print("_______________________________*WELCOME TO EMPLOYEE_MANAGEMENT_SYSTEM*________________________________________")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Search any Employee")
    print("3 to show all Employee's details")
    print("4 to Update Employee details")
    print("5  to Remove Employee ")
    print("6 to Exit")

    print("                                                     ***                                        ")
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Input_details()
    elif ch == 2:
        Search_employee()
    elif ch == 3:
        Get_Info()
    elif ch == 4:
        Update_employee()
    elif ch == 5:
        Remove_Employ()
    elif ch == 6:
        exit(0)
    else:   
        print("Invalid Choice")
main_function()






