from functools import reduce

l = [10,20,30]

def multiply(num1,num2):
    return num1 * num2

print(reduce(multiply,l))