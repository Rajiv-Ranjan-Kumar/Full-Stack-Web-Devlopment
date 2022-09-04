#Write a Python script to create a list of city names taken from the user.
n = int(input("Enter The Numbers of elements : "))
print("Enter The City Name : ")
list = []
for i in range(n):
    list.append(input())
print(list)