#Write a python script which takes a three digit number from the user and displays only its last digit.
num = int(input("Enter a Three Digit Number for Calculate Last Digit of a Number : "))
num %= 10
print("Last Digit Is %d"%num)
