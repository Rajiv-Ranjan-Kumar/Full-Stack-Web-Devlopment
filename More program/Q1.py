"""Write a program to iterate the first 10 numbers and in each iteration,
 print the sum of the current and previous number."""
for i in range(10):
    print("Number : %d previous number : %d  sum: %d" %
          (i, i if i == 0 else i-1, i if i == 0 else i-1+i))
