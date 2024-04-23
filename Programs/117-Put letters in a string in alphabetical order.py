# Examples
# alphabet_soup("hello") ➞ "ehllo"
# alphabet_soup("edabit") ➞ "abdeit"
# alphabet_soup("hacker") ➞ "acehkr"

def alphabet_soup(txt):
    return ''.join(sorted(txt))

print(alphabet_soup("hello"))
print(alphabet_soup("edabit"))
print(alphabet_soup("hacker"))