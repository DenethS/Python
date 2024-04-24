def sort_by_length(lst):
    return sorted(lst, key=len) # Using sorted function with a key

print(sort_by_length(["Google", "Apple", "Microsoft"]))
print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))