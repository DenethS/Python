# Examples
# index_of_caps("eDaBiT") ➞ [1, 3, 5]
# index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
# index_of_caps("determine") ➞ []
# index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
# index_of_caps("sUn") ➞ [1]

def index_of_caps(word):
    # Use list comprehension to find indices of capital letters
    return [i for i, char in enumerate(word) if char.isupper()]

print(index_of_caps("eDaBiT"))
print(index_of_caps("eQuINoX"))