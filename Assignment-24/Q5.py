# Write a python program to delete the age property of the user.
# create class
class DeleteAge:
    # create init method
    def __init__(self):
        self.name = "Rajiv Ranjan Kumar"
        self.age = 24
        self.email = 'rrks.195@gmail.com'


# create object
obj = DeleteAge()
del obj.age  # delete age property using del keyword
print(obj.age)
