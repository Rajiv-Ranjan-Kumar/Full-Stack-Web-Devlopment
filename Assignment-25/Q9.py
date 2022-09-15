"""Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry)."""


# create TrueCaller class
class TrueCaller:
    # create __init__() method
    def __init__(self):
        self.name = "Rajiv Singh"
        self.number = 8102471858

    # create nameFetching instance method
    def nameFetching(self):
        print("Name is Fetching by number....")

    # create addNew instance method
    def addNew(self):
        print("Add New..")


# create object of TrueCaller Class
tc = TrueCaller()

# method calling
tc.nameFetching()
tc.addNew()
