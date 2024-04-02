# # Example:
# # 5! = 5x4x3x2x1 = 120
# 0! is defined to be 1

def recur_factorial(n):
    if n ==1:
        return n
    else:
        return n*recur_factorial(n-1)
    
num = int(input("Enter the number: "))

#Check if its negative or a zero
if num < 0:
    print("The number does not exist for negative values")
elif num == 0:
    print("The factorial for 0 is 1")
else:
    print("The factorial for ", num, "is", recur_factorial(num))