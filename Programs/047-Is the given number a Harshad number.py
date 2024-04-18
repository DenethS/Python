# A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
# In other words, a number is considered a Harshad number if it can be evenly divided by the sum of its own digits.
# For example:
# 18 is a Harshad number because , and 18 is divisible by 9

def is_harshad_number(num):
    #Calculate the sum of the digits in the number
    digit_sum = sum(int(i) for i in str(num))

    #Check if the number is divisible by the sum of digits
    return num % digit_sum == 0

#Input a number
num = int(input("Enter a number: "))

#Check if it's a Harshad number
if is_harshad_number(num):
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")