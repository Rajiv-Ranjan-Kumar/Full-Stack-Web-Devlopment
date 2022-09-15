"""Write a python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller"""


# create class Calculator
class Calculator:
    # create add method
    def add(sef, num1, num2):
        print(num1 + num2)

    # create substract method
    def sub(self, num1, num2):
        print(num1 - num2)


# create class Calculator2.0
class Calculator_2(Calculator):

    # create multiply method
    def mul(sef, num1, num2):
        print(num1 * num2)

    # create division method
    def div(self, num1, num2):
        try:
            print(num1 / num2)
        except:
            print("Division not posible")


# create class Phone
class Phone:
    # create calling instance method
    def calling(self):
        print("Calling.....")

    # create sms instance method
    def sms(self):
        print("send sms...")


# create class SmartPhone
class SmartPhone(Calculator_2, Phone):

    # create trueCallerFetucher method for calling of nameFeatching method
    def trueCallerFetucher(self, id):
        id.nameFetching()


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
# create object of SmartPhone
sp = SmartPhone()

# method calling
sp.add(10, 20)
sp.sub(20, 10)
sp.mul(2, 30)
sp.div(10, 0)
sp.calling()
sp.sms()
sp.trueCallerFetucher(tc)
