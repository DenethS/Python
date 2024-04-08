#Split a string into a list of words
input_str = "Program to split and join a string"
word_list = input_str.split() #By default, split on whitespace

#Join the list of words into a string
separator = " " #Specify the separator between words
output_str = separator.join(word_list)

print("Original string: ", input_str)
print("List of split words: ", word_list)
print("Joined string: ", output_str)
