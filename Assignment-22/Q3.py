#Write a recursive python function to calculate sum of first N even natural numbers
def addEvennumber(num , sum = 0):
    if num == 0:
        return 0
    addEvennumber(num -1)
    if num % 2 == 0 :
        sum = num + addEvennumber(num-1,sum)
    else:
        sum = addEvennumber(num-1,sum)
    return sum

print("Sum = ",addEvennumber(int(input("Enter a Number : "))))