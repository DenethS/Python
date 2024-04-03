#Sample list of numbers
numbers = [23, 67, 32, 43]

#Sort the list in descending order
numbers.sort(reverse=True)

#Check if there are at least two elements in the list
if len(numbers) >=2:
    second_largest = numbers[1]
    print("The second largest number in the list is: ", second_largest)
else:
    print("The list does not contain a second largest number")