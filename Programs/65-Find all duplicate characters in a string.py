def find_duplicates(input_str):
    #Create an empty dictionary to store character counts
    char_count = {}

    #Initialize a list to store duplicate characters
    duplicates = []

    #Iterate through eachcharacter in the input string
    for char in input_str:
        #If the character is already in the dictionary, increment it's character count
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        #Iterate through the dictionary and add characters with the count of > 1
    for char, count in char_count.items():
        if count > 1:
             duplicates.append(char)
    return duplicates
    
#Input a string
input_string = "Llama workspace"

#Find duplicate characters in the string
duplicate_chars = find_duplicates(input_string)

#Print the list of duplicate characters
print("Duplicate characters: ", duplicate_chars)