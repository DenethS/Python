def remove_char(input_str, i):
    #Check if i is a valid index
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The string remains unchanged")

    #Remove the i-th character using slicing
    result_str = input_str[:i] + input_str[i + 1:]

    return result_str

#Input string
input_str = "Hello, Llama!"
i = 7 #Index of character to remove

#Remove the i-th character
new_str = remove_char(input_str, i)
print(f"Original string: {input_str}")
print(f"New string after removing {i}th character: {new_str}")