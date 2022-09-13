# Write a recursive python function to calculate sum of first N odd natural numbers
def addOddnumber(num , sum = 0):
    if num == 1:
        return 1
    addOddnumber(num -1)
    if num % 2 != 0 :
        sum = num + addOddnumber(num-1,sum)
    else:
        sum = addOddnumber(num-1,sum)
    return sum

print("Sum = ",addOddnumber(int(input("Enter a Number : "))))