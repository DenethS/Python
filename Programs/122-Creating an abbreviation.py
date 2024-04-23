# A group of friends have decided to start a secret society. The name will be the first
# letter of each of their names, sorted in alphabetical order. Create a function that takes
# in a list of names and returns the name of the secret society.
# Examples
# society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
# society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"

def society_name(names):
    # Extract the first letter of each name, sort them and join into an abbreviation
    secret_name = ''.join(sorted([name[0] for name in names]))
    return secret_name

print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", "Newt", "Luna", "Cho"]))