# Notes
# Return the elements in the list in alphabetical order.

def dict_to_list(input_dict):
    # Sort the dictionary by keys in alphabetical order
    sorted_dict = sorted(input_dict.items())

    # Convert the sorted dictionary to a list of tuples
    result = [(key, value) for key, value in sorted_dict]

    return result

print(dict_to_list({
    "D": 1, 
    "B": 2, 
    "C": 3

}))