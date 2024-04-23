# Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of compounding periods per year n. The function returns the value at the end of term rounded to the nearest cent.
# For the example:
# compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
# Note that the interest rate is given as a decimal and n=12 becaus with monthly compounding there are 12 periods per year. Compounding can also be done annually, quarterly, weekly, or daily.
# Examples
# compound_interest(100, 1, 0.05, 1) ➞ 105.0
# compound_interest(3500, 15, 0.1, 4) ➞ 15399.26
# compound_interest(100000, 20, 0.15, 365) ➞ 2007316.26

def compound_interest(p, t, r, n):
    # Calculate the compound interest usingthe formula
    a = p * (1 + (r / n)) ** (n * t)
    # Round the result to the nearest cent
    return round(a, 2)

print(compound_interest(10000, 10, 0.06, 12))
print(compound_interest(100000, 20, 0.15, 365))