# Q19: Check if a key exists in a dictionary.

dictionary = {}
for entry in input("Enter items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = value

key_to_find = input("Enter the key to check: ")
if key_to_find in dictionary:
    print("The key exists in the dictionary.")
else:
    print("The key does not exist in the dictionary.")