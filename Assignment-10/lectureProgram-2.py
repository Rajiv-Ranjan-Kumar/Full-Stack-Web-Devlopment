'''Write a program to print all the Character of a String,
but stop printing if 'r' appeared in the sequance if all the
charecter successfully printed the print message "All the
characters are processed"
'''
string = input("Enter the String : ")
for s in string :
    if s == 'r' :
        break;
    print(s,end=" ")
else:
    print("\n\nAll the characters are processed\n")