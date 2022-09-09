"""Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30."""
def square_of_list():
    list = [i**2 for i in range(2,30,1)]
    print(list)

square_of_list()