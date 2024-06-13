from math import factorial

import fibonacci

"""(1). Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination."""

year = int(input("Enter a year: "))
if year % 4 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
    print("It is divisible by 100")
elif year % 400 == 0:
    print(f"{year} is a leap year")

""" (2). Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3"""

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))
if side1 == side2 == side3 :
    print("The triangle is Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles")
elif side1 != side2 and side2 != side3 and side1 != side3:
    print("The triangle is Scalene")
else:
    print("Invalid input! Please enter valid side lengths.")


# (3). Factorial number
# Ex=   5! -->5*4*3*2*1 -> 120,  3! -> 3*2*1 -> 6,  4! -> 4*3*2*1 -> 24

num = int(input("Enter the Number : "))
result = factorial(num)
print(f"The factorial number of {num} is : {result}")


