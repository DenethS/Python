# Examples
# mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
# mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
# Notes
# All of the letters in the input list will always be lowercase.

def mapping(letters):
    result = {}
    for letter in letters:
        result[letter] = letter.upper()
        return result

print(mapping(["p", "s"]))
print(mapping(["a", "v", "y", "z"]))