# Examples
# replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
# replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

def replace_vowels(string, char):
    vowels = "AEIOUaeiou" # List of vowels to be replaced
    for vowel in vowels:
        string = string.replace(vowel, char) # Replace each vowel with a character
    return string

print(replace_vowels("the aardvark", "#"))
print(replace_vowels("homeowner", "@"))
print(replace_vowels("shakespeare", "*"))