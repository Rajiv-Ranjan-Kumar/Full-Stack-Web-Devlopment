"""Write a program to accept a string from the user and display characters that are present at an even index number."""
str1 = input("Enter a String : ")
for i in range(len(str1)):
    if i % 2 == 0:
        print(str1[i])
