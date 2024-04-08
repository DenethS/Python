def is_binary_str(input_str):
    #Iterate each character in the input string
    for i in input_str:
        #Checkif the i is not '0' or '1'
        if i not in '01':
            return False #If any character is not "0" or "1", it's not a binary string
    return True #If all characters are "0" or "1" it's a binary string

#Input string to check
input_str = "1001110"

#Check if the string is binary
if is_binary_str(input_str):
    print(f"{input_str} is a binary string")
else:
    print(f"{input_str} is not a binary string")