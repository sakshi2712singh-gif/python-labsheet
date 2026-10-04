# Q26: Write a program to convert a tuple of tuples into a dictionary.
count = int(input("How many key-value pairs? "))
pairs = ()

for number in range(count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    pairs += ((key, value),)

result = dict(pairs)
print("Tuple of tuples:", pairs)
print("Dictionary:", result)