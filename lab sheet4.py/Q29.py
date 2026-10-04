# Q29: Find common keys between two dictionaries.

first_dictionary = {}
second_dictionary = {}

for entry in input("Enter first dictionary items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    first_dictionary[key] = value

for entry in input("Enter second dictionary items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    second_dictionary[key] = value

common_keys = []
for key in first_dictionary:
    if key in second_dictionary:
        common_keys.append(key)

print("Common keys:", common_keys)