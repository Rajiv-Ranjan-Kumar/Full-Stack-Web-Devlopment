"""Write a python script to implement try except and else block for division"""


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
        else:
            x = input("Do You Want to Continue(Y/N): ")
            self.handleMultipleException() if x in ('Y', "y") else print("Thank You..")


# create object
obj = HandleMultipleException()
obj.handleMultipleException()
