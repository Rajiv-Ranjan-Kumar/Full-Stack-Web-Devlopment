#Create an endless iterator using generator method to produce Prime numbers
def primeGenerater():
    primeNo = 2
    while True:
        for i in range(2,primeNo,1):
            if primeNo % i == 0:
                break
        else:
            yield primeNo
        primeNo += 1

l = list()
it = primeGenerater()
while True:
    choice = input("Do You Want To Continue(Y/N): ")
    if choice in ('Y','y'):
        l.append(next(it))
    elif choice in ('N','n'):
        print(l,"\n Thak You...")
        break
    else:
        print("Wrong Choice..")