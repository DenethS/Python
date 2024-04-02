#Input two variables
a = input("Value of the first variable (a): ")
b = input("Value of the second variable (b): ")

#Display the original values
print(f"Original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
#Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")