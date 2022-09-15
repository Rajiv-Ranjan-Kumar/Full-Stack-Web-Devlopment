"""Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods(showConfig() to print the values, __init__() to initialize the
values).
"""


# create class
class Laptop:
    # create __init__(self) method for initialize the values
    def __init__(self):
        self.brand = "DEL"
        self.ram = "8 GB"
        self.cpu = "i9"
        self.hdd = "1 TB"

    # create showConfig() method for print the values
    def showConfig(self):
        print(self.brand, ":", self.ram, ":", self.cpu, ":", self.hdd)


# create class object
obj = Laptop()
obj.showConfig()  # call showConfig() method by class object
