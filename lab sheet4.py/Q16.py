# Q16: Sort a dictionary by values.

dictionary = {}
for entry in input("Enter items as key:number separated by spaces: ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = float(value)

sorted_items = sorted(dictionary.items(), key=lambda item: item[1])
sorted_dictionary = {}
for key, value in sorted_items:
    sorted_dictionary[key] = value

print("Dictionary sorted by values:", sorted_dictionary)