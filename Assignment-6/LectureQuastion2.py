"""
Write a Program to Print Grade Obtained in a Test. Take Marks Obtained from user and Display The Grade
        90 < marks <= 100   A
        80 < marks <= 90    B
        70 < marks <= 80    C
        60 < marks <= 70    D
        50 <= marks <= 60   E
        50 > marks          F
"""
marks = int(input("Enter a Total % of Marks for Calculate Grade : "))
if 90 < marks <= 100 :
    print("Grade A")
elif 80 < marks <= 90 :
    print("Grade B")
elif 70 < marks <= 80 :
    print("Grade C")
elif 60 < marks <= 70 :
    print("Grade D")
elif 50 <= marks <= 60 :
    print("Grade E")
elif 50 > marks :
    print("Grade F")
else :
    print("Please Enter Valide Marks")