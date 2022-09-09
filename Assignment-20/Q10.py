"""Write a python program to create a function to check whether a string is an anagram
or not"""
def anagram(string1,string2):
    set1 = {e for e in string1}
    set2 = {e for e in string2}
    if set1 == set2:
        print("Anagram")
    else :
        print("Not Anagram")

anagram(input("Enter First String : "),input("Enter Second String : "))