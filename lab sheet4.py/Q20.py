# Q20: Find the sum of all values in a dictionary.

dictionary = {}
for entry in input("Enter items as key:number separated by spaces: ").split():
    key, value = entry.split(":", 1)
    dictionary[key] = float(value)

total = 0
for value in dictionary.values():
    total += value

print("Sum of values:", total)