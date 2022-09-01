#Write a python script which takes a three digit number from the user and displays only its middle digit.
num = int(input("Enter a Three Digit Number for Calculate Middle Digit : "))
c = int(num / 10)
c %= 10
print(num,"Middle Digit Is %d"%c)
