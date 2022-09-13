# Create a generator to produce first n even natural numbers
def evenNoGenerater(num):
    smallEvenNo = 2
    while num > 0:
        yield smallEvenNo
        smallEvenNo += 2
        num -= 1

for e in evenNoGenerater(int(input("Enter a Number : "))):
    print(e)