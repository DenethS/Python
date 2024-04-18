# The natural logarithm, often denoted as , is a mathematical function that represents the
# logarithm to the base , where is the mathematical constant approximately equal to 2.71828
# . In other words, for a positive number , the natural logarithm of is the exponent that satisfies the equation e**y = x.
# Mathematically, the natural logarithm is expressed as:

# ln(x)

import math

num = float(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number")
else:
    result = math.log(num)
    print(f"The natutal logarithm of {num} is {result}")