#Create a generator to produce squares of first N natural numbers
def squareGenerater(num):
    number = 1
    while num > 0:
        yield number**2
        number += 1
        num -= 1

for e in squareGenerater(int(input("Enter a Number : "))):
    print(e)