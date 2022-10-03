""" Write a python script to handle multiple Exception in one try"""


# create class
class HandleMultipleException:
    # create method
    def handleMultipleException(self):
        try:
            num1 = int(input("Enter 1'st number : "))
            num2 = int(input("Enter 2'nd number : "))
            print("div = ", num1/num2)
        except ValueError:
            print("Please Enter only number")
        except ZeroDivisionError:
            print("Division not posible")
        except Exception:
            pass


# create object
obj = HandleMultipleException()
obj.handleMultipleException()
