"""Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
"""
year = int(input("Enter the Year : "))
match year :
    case year if year % 400 != 0 and year % 4 == 0 :
        print("%d Non Century leap Year" %year)
    case year if year % 400 == 0 and year % 4 == 0 :
        print("%d Century Leap Year" %year)
    case year if year % 400 != 0 and year % 4 != 0 :
        print("%d Non century non leap year" %year)
    case year if year % 400 == 0 and year % 4 != 0 :
        print("%d Century non leap year" %year)