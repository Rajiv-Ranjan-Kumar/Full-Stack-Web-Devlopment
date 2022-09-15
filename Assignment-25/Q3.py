# Write a python script to update 2nd Question, change email and age to __email and __age.
# create class Profile
class Profile:
    # create __init__() method
    def __init__(self):
        self.name = "Rajiv Singh"
        self.__email = None  # use __ for Private data
        self.__age = None

    # create setEmail method
    def setEmail(self, email):
        self.__email = email

    # create getEmail method
    def getEmail(self):
        return self.__email

    # create setAge method
    def setAge(self, age):
        self.__age = age

    # create getAge method
    def getAge(self):
        return self.__age


# create object
p = Profile()

# calling of method
p.setEmail(input("Enter Email : "))
p.setAge(int(input("Enter Age : ")))
print(p.name)
print(p.getEmail())
print(p.getAge())
