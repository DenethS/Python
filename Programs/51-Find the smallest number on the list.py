#Sample list of numbers
numbers = [10, -40, 12, -35]

#Initialize a variable to store the minimum value
minimum = numbers[0]

#Iterate through the list and update the minimum value
for i in numbers:
    if i < minimum:
        minimum = i

#Print the minimum value
print("The smallest number in the list is: ", minimum)        