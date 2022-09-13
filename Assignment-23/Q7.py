#Create an endless iterator using generator method to produce terms of Fibonacci series
def fibonacciGenerater():
    a,b = 0,1
    while True :
        yield a
        a,b = b,a+b

l = list()
it = fibonacciGenerater()
while True:
    choice = input("Do You Want To Continue(Y/N): ")
    if choice in ('Y','y'):
        l.append(next(it))
    elif choice in ('N','n'):
        print(l,"\n Thak You...")
        break
    else:
        print("Wrong Choice..")