# Write a recursive python function to print first N natural numbers.
def printNatualNo(num):
    if num > 0:
        printNatualNo(num - 1)
        print(num)

printNatualNo(int(input("Enter a Number : ")))