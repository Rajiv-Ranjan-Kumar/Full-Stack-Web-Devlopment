# Create a generator to produce first n odd natural numbers
def oddNoGenerater(num):
    smallOddNo = 1
    while num > 0:
        yield smallOddNo
        smallOddNo += 2
        num -= 1

for e in oddNoGenerater(int(input("Enter a Number : "))):
    print(e)