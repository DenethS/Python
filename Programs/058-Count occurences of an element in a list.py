def count_occurences(l, element):
    count = l.count(element)
    return count

#Example
my_list = [1, 2, 3, 6, 6, 5, 2, 4, 7, 5]
element_to_count = 5

occurences = count_occurences(my_list, element_to_count)
print(f"The element {element_to_count} appears {occurences} times")