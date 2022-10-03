# Write a python script to handle the ArithmeticError
# create ArithmeticErrorHandle class
class ArithmeticErrorHandle:
    # create arithmeticErrorHandle() method
    def arithmeticErrorHandle(self, num1, num2):
        try:
            print(num1/num2)
        except ArithmeticError:
            print("%d Is Not Divisible By %d" % (num1, num2))


# create class object
obj = ArithmeticErrorHandle()
obj.arithmeticErrorHandle(10, 0)
