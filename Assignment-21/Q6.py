#Write a recursive python function to print first N even natural numbers in reverse order.
def reverceEvenNo(num):
    if num < 1:
        return 1
    else:
        if num % 2 == 0:
            print(num)
    reverceEvenNo(num-1)

reverceEvenNo(int(input("Enter a Number : ")))