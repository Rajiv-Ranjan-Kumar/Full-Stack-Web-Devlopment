"""Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_number_in_list(list):
    for e in list:
        if e % 2 == 0:
            print(e)

even_number_in_list(list)