# Examples
# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
# filter_list(["A", 0, "Edabit", 1729, "Python", 1729]) ➞ [0, 1729]
# filter_list(["Nothing", "here"]) ➞ []

def filter_list(lst):
    # Use a list comprehension to filter out integers
    return [x for x in lst if isinstance(x, int)]

print(filter_list([1, 2, 3, 4, 'a', 'b']))