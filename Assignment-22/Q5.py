#Write a recursive python function to calculate sum of cubes of first N natural numbers
def sumOfCubes_N_netural(num , sum = 0):
    if num == 1:
        return 1
    sum = num**3 + sumOfCubes_N_netural(num - 1)
    return sum

print("Sum = ",sumOfCubes_N_netural(int(input("Enter a Number : "))))