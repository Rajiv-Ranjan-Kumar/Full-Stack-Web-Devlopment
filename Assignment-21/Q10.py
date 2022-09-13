# Write a recursive python function to print a number in reverse order.

def printReverceOrder(num , rev = 0):
    if num <= 0:
        print("reverce = ",rev)
        return 1
    else:
        printReverceOrder(num // 10 , rev * 10 + num % 10)

printReverceOrder(int(input("Enter a Number : ")))