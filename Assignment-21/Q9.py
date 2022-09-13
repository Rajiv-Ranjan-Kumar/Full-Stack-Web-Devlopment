#Write a recursive python function to print first N multiples of a given number.
def multipalGivenNo(num , temp = 0):
    if temp == 0:
        temp = num
    if num <= 0:
        return 1
    else:
        multipalGivenNo(num - 1 , temp)
        print("%d * %d = %d" %(num,temp,num * temp))

multipalGivenNo(int(input("Enter a Number : ")))