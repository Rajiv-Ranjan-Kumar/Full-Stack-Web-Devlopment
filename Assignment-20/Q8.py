"""Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.
"""
def calculate(string):
    count , count1 = 0 , 0
    for e in string:
        if ord(e) in range(65,91,1):
            count += 1
        if ord(e) in range(97,123,1):
            count1 += 1
    print("Total Upper Case = ",count,"\nTotal Lower Case = ",count1)

calculate(input("Enter a String : "))