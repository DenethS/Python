def find_words(words, k):
    result = []
    #Create an empty list to store words greater than k

    #Iterate through each word in the list
    for i in words:
        #Check if the lrngth of the i is greater than k
        if len(i) > k:
            result.append(i)

    return result

#Example
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
k = 6
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters are {long_words}")