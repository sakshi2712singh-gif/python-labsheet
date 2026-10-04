# Q15: Sort a dictionary by keys.

dictionary = {}
for entry in input("Enter items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = value

sorted_dictionary = {}
for key in sorted(dictionary):
    sorted_dictionary[key] = dictionary[key]

print("Dictionary sorted by keys:", sorted_dictionary)