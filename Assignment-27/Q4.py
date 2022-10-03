# Write a python script to handle a ValueError
# create ValueErrorHandle class
class ValueErrorHandle:
    # create valueErrorHandle() method
    def valueErrorHandle(self):
        num = None
        try:
            num = int(input("Enter a number : "))
        except ValueError:
            print("Only Enter a Integer")


# create object
obj = ValueErrorHandle()
obj.valueErrorHandle()
