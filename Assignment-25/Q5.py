"""Write a python script to create a Calculator class with 2 methods for adding and
subtracting 2 values.
"""


# create class
class Calculator:

    # create add method
    def add(sef, num1, num2):
        return num1 + num2

    # create substract method
    def sub(self, num1, num2):
        return num1 - num2


# create object
c = Calculator()

# method calling
value1 = c.add(20, 10)
value2 = c.sub(30, 50)
# print values
print(value1, value2, sep="\n")
