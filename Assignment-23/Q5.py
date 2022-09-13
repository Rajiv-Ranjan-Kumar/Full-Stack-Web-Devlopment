# Create a generator to produce first n terms of Fibonacci series
def fibonacciGenerater(num):
    a,b = 0,1
    while num > 0 :
        yield a
        a,b = b,a+b
        num -= 1

for e in fibonacciGenerater(int(input("Enter a Number : "))):
    print(e)