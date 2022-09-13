# create a generater to produce first n even netural numbers
def evenGenerater(num):
    smallEven = 2
    while num > 0:
        yield smallEven
        smallEven += 2
        num -= 1

for e in evenGenerater(int(input("Enter a Number : "))):
    print(e)
