# With Python 3, you can assign variables from lists in a succinct way.
# Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:
# first ➞ 1
# middle ➞ [2, 3, 4, 5]
# last ➞ 6

writeyourcodehere = [1, 2, 3, 4, 5, 6]

#Unpack the list into variables
first, *middle, last = writeyourcodehere

print(first)
print(middle)
print(last)