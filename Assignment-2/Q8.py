"""
Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py
"""

from a import x as X
x = 20
print(X)
print(x)