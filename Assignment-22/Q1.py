#Write a recursive python function to calculate sum of first N natural numbers
def sumOf_N_netural(num , sum = 0):
    if num == 1:
        return 1
    sum = num + sumOf_N_netural(num - 1)
    return sum

print("Sum = ",sumOf_N_netural(int(input("Enter a Number : "))))