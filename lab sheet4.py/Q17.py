# Q17: Update the value of a key in a dictionary.

dictionary = {}
for entry in input("Enter items as key:value separated by spaces: ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = value

key_to_update = input("Enter the key to update: ")
new_value = input("Enter the new value: ")

if key_to_update in dictionary:
    dictionary[key_to_update] = new_value
    print("Updated dictionary:", dictionary)
else:
    print("Key not found. Dictionary unchanged:", dictionary)