# Write a python script to raise a ValueError

# create class
class HandleMultipleException:
    # create method
    def handleMultipleException(self):
        num1 = int(input("Enter 1'st number : "))
        num2 = int(input("Enter 2'nd number : "))
        if num2 == 0:
            raise Exception("Division By Zero Not Posible.")
        else:
            print("div = ", num1/num2)


# create object
obj = HandleMultipleException()
obj.handleMultipleException()
