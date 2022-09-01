#Write a program to count 'a' in a given string using for loop
string = input("Enter a String : ")
c = 0
for i in string :
    if i == 'a' :
        c += 1
print(c)