"""Write a python program to create a function to check whether a string is a pangram
or not."""

def pangram(string):
    list = []
    for e in string:
        if ord(e) in range(65,91,1) or ord(e) in range(97,123,1):
            if e not in list:
                list.append(e)

    if len(list) == 26:
        print("Pangram String")
    else :
        print("Not Pangram String")

pangram(input("Enter a String : "))