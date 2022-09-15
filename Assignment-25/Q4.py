# Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.

# create class Profile
class Profile:
    # create class variable
    platform = "program"

    # create __init__() method
    def __init__(self):
        self._name = None  # use _ as a treat
        self._email = None  # Private data but
        self._age = None  # not private data means data is protected

    # create setName method
    def setName(self, name):
        self._name = name

    # create getName method
    def getName(self):
        return self._name

    # create setEmail method
    def setEmail(self, email):
        self._email = email

    # create getEmail method
    def getEmail(self):
        return self._email

    # create setAge method
    def setAge(self, age):
        self._age = age

    # create getAge method
    def getAge(self):
        return self._age

    # create class method
    @classmethod
    def platformAcces(cls):  # cls is a short form of class
        print(cls.platform)


# create object
p = Profile()

# calling of method
p.setName(input("Enter Name : "))
p.setEmail(input("Enter Email : "))
p.setAge(int(input("Enter Age : ")))
print(p.getName())
print(p.getEmail())
print(p.getAge())
Profile.platformAcces()
