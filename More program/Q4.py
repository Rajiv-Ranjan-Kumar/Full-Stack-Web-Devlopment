"""Write a function to return True if the first and last number of a given list is same.
If numbers are different then return False."""

list1 = [10, 20, 30, 40, 50, 60, 10]
list2 = [10, 20, 30, 40, 50, 60, 70]


def check(list1):
    if list1[0] == list1[-1]:
        return True
    else:
        return False


def check2(list2):
    if list2[0] == list2[-1]:
        return True
    else:
        return False


print(check(list1))
print(check2(list2))
