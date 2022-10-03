"""Write a python script to add a finally block for the above script
"""

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
        finally:
            input("thank youu..\n\tExit for press Enter")


# create object
obj = HandleMultipleException()
obj.handleMultipleException()
