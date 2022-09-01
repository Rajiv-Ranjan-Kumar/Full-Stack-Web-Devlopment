"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""
age = int(input("Enter the Age : "))
match age :
    case age if age > 0 and age < 10 :
        print("kid")
    case age if age >= 10 and age < 20 :
        print("Teen")
    case age if age >= 20 and age < 40 :
        print("Young")
    case age if age >=40 and age < 60 :
        print("Experienced")
    case _ :
        print("Senior Citizen")