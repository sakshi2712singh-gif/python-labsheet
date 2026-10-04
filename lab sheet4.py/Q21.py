# Q21: Find the key with the maximum value in a dictionary.

dictionary = {}
for entry in input("Enter items as key:number separated by spaces: ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = float(value)

if dictionary:
    largest_key = max(dictionary, key=dictionary.get)
    print("Key with the maximum value:", largest_key)
    print("Maximum value:", dictionary[largest_key])
else:
    print("The dictionary is empty.")