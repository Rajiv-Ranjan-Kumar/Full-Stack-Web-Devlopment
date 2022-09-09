"""Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements."""

list = [10,20,30,15,25,35,40,45]
print("Original list\n",list)
def even_element_of_list(list):
    list = [e for e in list if e % 2 == 0]
    return list

list = even_element_of_list(list)
print("Unique List\n",list)