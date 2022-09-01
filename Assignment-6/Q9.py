#Write a python script to check whether a given year is a leap year or not.
year = int(input("Enter the Year : "))
if year % 4 == 0 and year % 400 == 0 :
    print(year," Is a Leap Year")
else :
    print(year,"Is not Leap Year")