# Write a python script to update the above Profile class with encapsulation.
# create class Profile
class Profile:
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


# create object
p = Profile()

# calling of method
p.setName(input("Enter Name : "))
p.setEmail(input("Enter Email : "))
p.setAge(int(input("Enter Age : ")))
print(p.getName())
print(p.getEmail())
print(p.getAge())
