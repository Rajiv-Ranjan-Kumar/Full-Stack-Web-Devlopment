"""Write a python script to implemented a nested Try Except block"""


# create class
class HandleMultipleException:
    # create method
    def handleMultipleException(self):
        try:
            num1 = int(input("Enter 1'st number : "))
            num2 = int(input("Enter 2'nd number : "))
            try:
                print("div = ", num1/num2)
            except ZeroDivisionError:
                print("Divisition not posible")
        except ValueError:
            print("Please Enter only number")


# create object
obj = HandleMultipleException()
obj.handleMultipleException()
