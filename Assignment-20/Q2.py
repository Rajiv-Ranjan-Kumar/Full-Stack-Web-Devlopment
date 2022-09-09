"""Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.
"""

def check_prime_no(num):
    flag = 0
    for i in range(2,num):
        if num % i == 0:
            flag = 1
            continue
    print("Peime Number" if flag == 0 else "Not Prime Number") 
    
check_prime_no(int(input("Enter a Number : ")))