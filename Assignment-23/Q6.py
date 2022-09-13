#Create a generator to produce first n prime numbers
def primeGenerater(num):
    primeNo = 2
    while primeNo <= num:
        for i in range(2,primeNo,1):
            if primeNo % i == 0:
                break
        else:
            yield primeNo
        primeNo += 1

for e in primeGenerater(int(input("Enter a Number : "))):
    print(e)