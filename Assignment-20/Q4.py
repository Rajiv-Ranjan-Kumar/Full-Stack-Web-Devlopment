"""Write a python program to create a function that checks whether a passed string is
palindrome or not."""

def check_palindrome(string):
    if string == string[::-1]:
        print("Palindrome String")
    else :
        print("Not Palindrome String")

check_palindrome(input("Enter a String : "))