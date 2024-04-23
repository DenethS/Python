# Examples
# is_symmetrical(7227) ➞ True
# is_symmetrical(12567) ➞ False
# is_symmetrical(44444444) ➞ True
# is_symmetrical(9939) ➞ False

def is_symmetrical(num):
    # Convert the number to a string
    num_str = str(num)

    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

print(is_symmetrical(7227))
print(is_symmetrical(12567))
print(is_symmetrical(44444444))