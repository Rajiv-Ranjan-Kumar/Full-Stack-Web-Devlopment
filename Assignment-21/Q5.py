#Write a recursive python function to print first N even natural numbers.
def evenNo(num):
    if num > 0:
        evenNo(num-1)
        if num % 2 == 0:
            print(num)

evenNo(int(input("Enter a Number : ")))