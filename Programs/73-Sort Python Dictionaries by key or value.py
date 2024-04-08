#Sort by keys
sample_dict = {'banana': 1, 'cherry': 2, 'date': 4, 'apple': 3}

sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print("Sorted by keys: ")
for key, value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")