#Write a python script to create a Profile class with 3 attributes (name, email, age).
#create class Profile
class Profile:
    #create __init__() method
    def __init__(self) :
        self.name = "Rajiv Ranjan Kumar"
        self.email = 'rrks.195@gmail.com'
        self.age = 24

#create object
p = Profile()

#print all attributes values
print(p.name)
print(p.email)
print(p.age)