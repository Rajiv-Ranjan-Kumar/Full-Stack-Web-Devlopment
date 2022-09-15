"""WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size. 
"""


# create class
class Laptop:
    # create list
    l1 = list()
    l2 = list()
    l3 = list()

    # create __init__(self) method for initialize the values
    def __init__(self):
        self.brand = "DEL"
        self.ram = "8 GB"
        self.cpu = "i9"
        self.hdd = "1 TB"

    # store the values
    def storeValues(self):
        if self.ram == "8 GB":
            Laptop.l1.append(self.brand)
            Laptop.l1.append(self.ram)
            Laptop.l1.append(self.cpu)
            Laptop.l1.append(self.hdd)
        elif self.ram == "4 GB":
            Laptop.l2.append(self.brand)
            Laptop.l2.append(self.ram)
            Laptop.l2.append(self.cpu)
            Laptop.l2.append(self.hdd)
        else:
            Laptop.l3.append(self.brand)
            Laptop.l3.append(self.ram)
            Laptop.l3.append(self.cpu)
            Laptop.l3.append(self.hdd)

    # create showConfig() method for print the values
    def showConfig(self):
        print(Laptop.l1, Laptop.l2, Laptop.l3, sep="\n")


# create class object
obj1 = Laptop()
obj2 = Laptop()
obj3 = Laptop()

obj1.storeValues()
obj2.ram = "16 GB"
obj2.storeValues()
obj3.ram = "4 GB"
obj3.storeValues()

obj1.showConfig()  # call showConfig() method by class object
