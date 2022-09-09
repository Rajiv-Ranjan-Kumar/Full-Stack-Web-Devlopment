#write a python script input the list from user
str = input("Enter the list element sepreted by comma : ")
strlist = [eval(x) for x in str.split(",")]
print(strlist)