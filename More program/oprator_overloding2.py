class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        total_num1 = self.num1 + other.num1
        total_num2 = self.num2 + other.num2
        return total_num1+total_num2

    def __sub__(self, other):
        total_num1 = self.num1 - other.num1
        total_num2 = self.num2 - other.num2
        return total_num1-total_num2

    def __mul__(self, other):
        total_num1 = self.num1 * other.num1
        total_num2 = self.num2 * other.num2
        return total_num1 * total_num2

    def __truediv__(self, other):
        try:
            total_num1 = self.num1 / other.num1
            total_num2 = self.num2 / other.num2
            return total_num1 / total_num2
        except Exception:
            pass


num1 = Calculator(10, 20)
num2 = Calculator(20, 10)
print("Sum = ", num1 + num2)
print("Sub = ", num1 - num2)
print("Mul = ", num1 * num2)
print("Div = ", num1 / num2)
