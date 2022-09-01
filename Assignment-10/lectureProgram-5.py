'''Write a program to print first N even netural numbers.
in reverce order'''
num = int(input("Enter a Number : "))
for i in range(num) :
    if i % 2 != 0 :
        i += 1
        continue
    print(num-i)
    i += 1