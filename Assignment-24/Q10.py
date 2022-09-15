"""Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values"""
# create class


class Employee:
    # create __init__()method
    def __init__(self):
        self.empid = None
        self.name = None
        self.salary = None

    # create instance method for get details by user
    def getDetail(self):
        self.empid = input("Enter Employee Id : ")
        self.name = input("Enter Employee Name : ")
        self.salary = float(input("Enter Employee Salary : "))

    # create instace method for print data
    def disp(self):
        print("Employe Id : ", self.empid)
        print("Employe Name : ", self.name)
        print("Employe Salary : ", self.salary)


# create object
obj = Employee()

# call instance method
obj.getDetail()
obj.disp()
