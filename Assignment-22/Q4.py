#Write a recursive python function to calculate sum of squares of first N natural numbers
def squareSumOf_N_netural(num , sum = 0):
    if num == 1:
        return 1
    sum = num**2 + squareSumOf_N_netural(num - 1)
    return sum

print("Sum = ",squareSumOf_N_netural(int(input("Enter a Number : "))))