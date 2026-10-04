# Q18: Remove a key from a dictionary.

dictionary = {}
for entry in input("Enter items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = value

key_to_remove = input("Enter the key to remove: ")
if key_to_remove in dictionary:
    del dictionary[key_to_remove]
    print("Updated dictionary:", dictionary)
else:
    print("Key not found. Dictionary unchanged:", dictionary)