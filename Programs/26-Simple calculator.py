#import from numpy otherwise won't work
from numpy import divide
from numpy import multiply

#Addition
def add(x, y):
    return x + y

#Substraction
def substract(x, y):
    return x - y

#Multiplication
def multiplication(x, y):
    return x * y

#Division
def division(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

while True:
    #take input
    choice = input("Enter choice (1/2/3/4): ")

    #Check if it's within range
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == "2":
        print(num1, "-", num2, "=", substract(num1, num2)) 

    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2)) 

    elif choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))

    #If user doesn't want another operation, break the for loop
    next_calculation = input("Next calculation? (y/n): ")
    if next_calculation == "n":
        break
    else:
        print("Invalid input")