# Write a recursive python function to print first N natural numbers in reverse order
def reverceNetural(num):
    if num > 0 :
        print(num)
        reverceNetural(num - 1)

reverceNetural(int(input("enter a Number : ")))