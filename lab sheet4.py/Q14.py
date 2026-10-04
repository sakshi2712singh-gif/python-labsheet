# Q14: Merge two dictionaries into one.

first_dictionary = {}
second_dictionary = {}

for entry in input("Enter first dictionary items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    first_dictionary[key] = value

for entry in input("Enter second dictionary items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    second_dictionary[key] = value

merged_dictionary = first_dictionary.copy()
for key in second_dictionary:
    merged_dictionary[key] = second_dictionary[key]

print("Merged dictionary:", merged_dictionary)