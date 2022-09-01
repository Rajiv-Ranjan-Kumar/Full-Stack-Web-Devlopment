#write a progra to print first n even netural numbers.
num = int(input("Enter a number : "))
i = 1
while i <= num :
    if i % 2 == 0 :
        print(i)
    i += 1