"""Write a python program to init default values for user object using __init__ method"""


# create class
class UserDetail:
    # create init method
    def __init__(self):
        # set default values of variables
        self.name = None
        self.rollNo = None
        self.email = None


# create object
obj = UserDetail()

# print default values
print(obj.name)
print(obj.rollNo)
print(obj.email)
