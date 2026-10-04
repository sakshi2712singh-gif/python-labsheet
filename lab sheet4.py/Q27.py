# Q27: Remove duplicate values from a dictionary.

dictionary = {}
for entry in input("Enter items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = value

unique_dictionary = {}
seen_values = []
for key, value in dictionary.items():
    if value not in seen_values:
        unique_dictionary[key] = value
        seen_values.append(value)

print("Dictionary without duplicate values:", unique_dictionary)