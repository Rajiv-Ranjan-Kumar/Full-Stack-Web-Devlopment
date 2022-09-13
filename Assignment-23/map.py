l = [1,2,3,4,5,6,7,8,9]#list

def square(num): #function
    return num**2

l1 = list(map(square,l)) #use maip function
print(l1)