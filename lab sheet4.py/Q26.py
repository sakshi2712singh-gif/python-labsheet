# Q26: Check if two dictionaries are equal.

first_dictionary = {}
second_dictionary = {}

for entry in input("Enter first dictionary items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    first_dictionary[key] = value

for entry in input("Enter second dictionary items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    second_dictionary[key] = value

if first_dictionary == second_dictionary:
    print("The dictionaries are equal.")
else:
    print("The dictionaries are not equal.")