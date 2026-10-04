# Q9: Flatten a nested list.

rows = input("Enter rows separated by semicolons, with items separated by spaces: ").split(";")
nested_list = []

for row in rows:
    nested_list.append(row.split())

flat_list = []
for row in nested_list:
    for item in row:
        flat_list.append(item)

print("Nested list:", nested_list)
print("Flattened list:", flat_list)