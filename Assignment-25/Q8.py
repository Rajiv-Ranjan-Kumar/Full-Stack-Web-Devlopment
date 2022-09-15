"""Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
Phone Class.
"""


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
    pass


# create object of SmartPhone
sp = SmartPhone()

# method calling
sp.add(10, 20)
sp.sub(20, 10)
sp.mul(2, 30)
sp.div(10, 0)
sp.calling()
sp.sms()
