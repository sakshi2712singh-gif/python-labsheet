# Q27: Write a program to unzip a list of tuples into individual lists.
count = int(input("How many pairs of items? "))
pairs = []

for number in range(count):
    first, second = input("Enter two items separated by a space: ").split()
    pairs.append((first, second))

first_items = []
second_items = []
for first, second in pairs:
    first_items.append(first)
    second_items.append(second)

print("First list:", first_items)
print("Second list:", second_items)