# Examples
# next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
# next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
# next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
# next_in_line([], 6) ➞ "No list has been selected"

def next_in_line(lst, num):
    if lst:
        lst.pop(0) # Remove the first element
        lst.append(num) # Add the number to the end
        return lst
    else:
        return "No list has been selected"
    
print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))