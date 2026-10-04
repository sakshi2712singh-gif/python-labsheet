# Q23: Convert two lists into a dictionary.

keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()

if len(keys) != len(values):
    print("The lists must have the same number of items.")
else:
    dictionary = {}
    for index in range(len(keys)):
        dictionary[keys[index]] = values[index]
    print("Dictionary:", dictionary)