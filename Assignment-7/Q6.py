"""Write a python program to check whether a given string is a multiword string or single
word string using match case statement
"""
string = input("Enter the String : ")
string = string.strip()
match string :
    case string if " " in string or "@" in string or "#" in string or "$" in string or "%" in string or "&" in string or "*" in string:
        print("multiword string")
    case _ :
        print("Single String")