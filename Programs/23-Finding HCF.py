#HCF, or Highest Common Factor, is the largest positive integer that divides two or more
#numbers without leaving a remainder.

#For two numbers a and b, the HCF can be found using the formula:

#HCF(a, b) = GCD(a, b)

#For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers at
#a time until you reach the last pair.
#Note: GCD stands for Greatest Common Divisor.

#Find HCF of two numbers

def compute_hcf(x, y):
    if x > y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input("Enter the number a: "))
num2 = int(input("Enter the number b: "))

print("The HCF is ", compute_hcf(num1, num2))