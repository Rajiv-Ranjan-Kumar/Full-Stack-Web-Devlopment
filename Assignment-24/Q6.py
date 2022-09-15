# Write a python program to create 3 user objects and find the youngest of all.
# create class
class SetYoungestData:
    # create init method
    def __init__(self, name, age, email):
        # set the values of instance variables
        self.name = name
        self.age = age
        self.email = email

    # create method for fiend the max age
    def findYoungest(self, age2, age3):
        self.age2 = age2
        self.age3 = age3
        return max(self.age, self.age2, self.age3)


# create objects
obj1 = SetYoungestData('Rajiv', 24, 'rrks.195@gmail.com')
obj2 = SetYoungestData('Ranjan', 25, 'rajiv195@gamil.com')
obj3 = SetYoungestData('Rahul', 30, 'rahul123@gmail.com')

maxAge = obj1.findYoungest(obj2.age, obj3.age)  # call the fiendYoungest method

# print youngest data
if maxAge == obj1.age:
    print(obj1.name, "\n", obj1.age, "\n", obj1.email)
elif maxAge == obj2.age:
    print(obj2.name, "\n", obj2.age, "\n", obj2.email)
else:
    print(obj3.name, "\n", obj3.age, "\n", obj3.email)
