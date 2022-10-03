from logging import exception


class OperatorOverloding:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        try:
            return self.num / other.num
        except exception:
            pass

    def __floordiv__(self, other):
        try:
            return self.num // other.num
        except exception:
            pass

    def __mod__(self, other):
        return self.num % other.num

    def __pow__(self, other):
        return self.num**other.num

    def __rshift__(self, other):
        return self.num >> other.num

    def __lshift__(self, other):
        return self.num << other.num

    def __and__(self, other):
        return self.num & other.num

    def __or__(self, other):
        return self.num | other.num

    def __xor__(self, other):
        return self.num ^ other.num


op = OperatorOverloding(10)
op1 = OperatorOverloding(20)
print(op+op1)
print(op-op1)
print(op*op1)
print(op/op1)
print(op//op1)
print(op % op1)
print(op**op1)
print(op >> op1)
print(op << op1)
print(op & op1)
print(op | op1)
print(op ^ op1)
