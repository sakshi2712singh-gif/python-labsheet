# Q22: Write a program to flatten a nested tuple.
rows = input("Enter each row's items separated by spaces, and rows by semicolons: ").split(";")
nested = ()

for row in rows:
    nested += (tuple(row.split()),)

flattened = ()
for row in nested:
    for item in row:
        flattened += (item,)

print("Nested tuple:", nested)
print("Flattened tuple:", flattened)