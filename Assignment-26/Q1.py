"""Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
a class using method overloading."""


class Multiplication:
    def mul(self, num1, num2, num3=1, num4=1):
        return num1 * num2 * num3 * num4


m = Multiplication()
print(m.mul(10, 20))
print(m.mul(10, 20, 30))
print(m.mul(10, 20, 30, 40))
