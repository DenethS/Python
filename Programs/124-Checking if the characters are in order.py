# Examples
# is_in_order("abc") ➞ True
# is_in_order("edabit") ➞ False
# is_in_order("123") ➞ True
# is_in_order("xyzz") ➞ True

# Notes
# You don't have to handle empty strings.

def is_in_order(s):
    return s == ''.join(sorted(s))

print(is_in_order("abc"))
print(is_in_order("edabit"))