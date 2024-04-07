def find_n_largest_numbers(lst, n):
    #Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)

    #Get the first N elements
    largest_elements = sorted_lst[:n]
    return largest_elements

#Sample list of numbers
numbers = [30, 10, 45, 75, 98, 2, 80, 45, 178, 898, 167]

#Number of largest elements to find
N = int(input("N = "))

#Find the N largest elements from the list
result = find_n_largest_numbers(numbers, N)

#Print the N largest elements
print(f"The {N} largest elements in the list are: ", result)