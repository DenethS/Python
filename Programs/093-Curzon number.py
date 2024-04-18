# If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

# If (2^n + 1) is divisible by (2n + 1), then 'n' is a Curzon number.

# Examples
# is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

def is_curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0

# Test cases
print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))