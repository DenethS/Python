import re

def check_special_char(in_str):
    #Define a regular expression pattern to match special characters
    pattern = r'[!@#$%^&*()]'

    #Use re.search to find a match in the input string
    if re.search(pattern, in_str):
        return True
    else:
        return False

#Input a string
input_string = str(input("Enter a string: "))

#Check if the string contains special characters
contains_special = check_special_char(input_string)

if contains_special:
    print("The string contains special characters")
else:
    print("The string does not contain special characters")
