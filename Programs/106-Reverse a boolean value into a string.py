# Examples
# reverse(True) ➞ False
# reverse(False) ➞ True
# reverse(0) ➞ "boolean expected"
# reverse(None) ➞ "boolean expected"


def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"
    
print(reverse(True))
print(reverse(0))
print(reverse(None))