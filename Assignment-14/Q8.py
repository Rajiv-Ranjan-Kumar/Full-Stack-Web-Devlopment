"""Write a Python script to print distinct elements along with their frequencies of
occurrence in the list"""
list = [10,10,10,20,20,30.50,30.50,"Rajiv",6+8j,6+8j,80]
list1 = []
list1.append(list[0])
for i in list :
    x = list1.count(i)
    if x == 0:
        list1.append(i)

print("distinct elements\tfrequencies")
for i in list1:
    print(i,list.count(i),sep="\t\t\t")
