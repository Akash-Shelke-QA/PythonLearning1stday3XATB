#Explain the difference between the = operator and the == operator in Python.
"""= is assign the value into the veriable
 EX= A = 10
 == is compare the value of two veriables which is return bool
 a == 9 """

#What does the ** operator do in Python, and how is it used?
"""** is used to raising first operand to the power of second operand 
EX= 4**2 = 16 """


#What does the ^ operator do in Python, and in what context is it commonly used?
"""it is XOR binary operator """

# Task 2-------------------
# 1.Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

#square 
num = input("Enter a number: ")
num = int(num)

sq = num ** 2
print(f"The Square of the {num} is {sq}")

a =sq -4
print(a)
#cube
cube = num ** 3
print(f"The Cube of the {num} is {cube}")

#2. Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

first_num = input("Enter a number: ")
Second_num = input("Enter a number: ")
first_num = int(first_num)
Second_num = int(Second_num)

print(first_num > Second_num)
print(first_num < Second_num)
print(first_num == Second_num)

