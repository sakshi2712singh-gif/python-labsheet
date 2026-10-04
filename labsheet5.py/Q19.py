# Q19: Write a program to remove duplicate elements from a tuple.
values = tuple(input("Enter tuple items separated by spaces: ").split())
unique_values = ()

for item in values:
    if item not in unique_values:
        unique_values += (item,)

print("Tuple without duplicates:", unique_values)