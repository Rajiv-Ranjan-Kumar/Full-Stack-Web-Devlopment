#Write a recursive python function to find the Nth term of the Fibonacci series
def fibonacci(num,a=0,b=1):
    if num == 0:
        return 0
    if num > 2:
        print(a+b)
        temp = a
        a = b
        b = b + temp       
        fibonacci(num-1,a,b)

x = int(input("Enter a Number : "))
print(0)
print(1)
fibonacci(x)