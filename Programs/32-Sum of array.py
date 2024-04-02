#Finding sum of array
x = 1
y = 2
z = 3
arr = [x, y, z]
ans = sum(arr)
print("Sum of the array is ", ans)

#Function to find the sum of elements in the array
def sum_of_array(arr):
    total = 0 #Initialize a variable to store the sum - starts from 0 to start the sum from the beginning before the summation process
    for element in arr:
        total += element #Add each element to the total
    return total

#Example
arr = [7, 9, 3]
result = sum_of_array(arr)
print("The sum of the array is ", result)