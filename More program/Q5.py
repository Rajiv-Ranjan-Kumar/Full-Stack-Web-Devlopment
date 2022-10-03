# Iterate the given list of numbers and print only those numbers which are divisible by 5
list1 = [5, 10, 13, 14, 15, 16, 17, 18, 20, 24, 26, 28]
for e in list1:
    if e % 5 == 0:
        print(e, end=" ")
