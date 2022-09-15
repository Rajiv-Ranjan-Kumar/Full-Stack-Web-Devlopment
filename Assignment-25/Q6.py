"""Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class.
"""


# create class Calculator
class Calculator:
    # create add method
    def add(sef, num1, num2):
        return num1 + num2

    # create substract method
    def sub(self, num1, num2):
        return num1 - num2


# create class Calculator2.0
class Calculator_2(Calculator):

    # create multiply method
    def mul(sef, num1, num2):
        return num1 * num2

    # create division method
    def div(self, num1, num2):
        try:
            return num1 / num2
        except:
            pass


# create object
c = Calculator_2()

# method calling
value1 = c.add(20, 10)
value2 = c.sub(30, 50)
value3 = c.mul(2, 3)
value4 = c.div(6, 0)

# print values
print("Sum = ", value1, "\nSub = ", value2,
      "\nMul = ", value3, "\nDiv = ", value4)
