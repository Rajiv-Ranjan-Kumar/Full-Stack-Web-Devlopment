"""Write a python program to create a School class and 3 instance variables and 1 class
variable."""


# create class
class School:
    # create class variable
    schoolName = "R.N HIGH SCHOOL JAKHIM"

    # create __init__()method
    def __init__(self):
        # create instance variable
        self.name = "Rajiv Ranjan Kumar"
        self.department = "Science"
        self.rollNo = 23


# create object
obj = School()

# print All Data
print("School : ", School.schoolName)
print("Name : ", obj.name)
print("Department : ", obj.department)
print("Roll No. : ", obj.rollNo)
