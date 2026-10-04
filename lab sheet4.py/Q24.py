# Q24: Invert a dictionary (keys become values and values become keys).

dictionary = {}
for entry in input("Enter items as key:value separated by spaces (values should be unique): ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = value

inverted_dictionary = {}
for key, value in dictionary.items():
    inverted_dictionary[value] = key

print("Inverted dictionary:", inverted_dictionary)