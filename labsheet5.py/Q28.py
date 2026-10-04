# Q28: Write a program to find repeated items in a tuple.
values = tuple(input("Enter tuple items separated by spaces: ").split())
repeated = ()

for item in values:
    if values.count(item) > 1 and item not in repeated:
        repeated += (item,)

print("Repeated items:", repeated)