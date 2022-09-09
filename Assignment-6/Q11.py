"""
Write a python script to take the month value in numeric format and display the
number of days in it.
"""
num = int(input("Enter a Month Value in Numeric Format : "))
if num == 1 or num == 3 or num == 5 or num == 7 or num == 9 or num == 11 :
    print("31 Day's")
elif num == 2 :
    print("28 or 29 day's")
else :
    print("30 Day's")