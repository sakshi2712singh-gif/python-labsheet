# Q5: Write a program to access tuple elements using slicing.
values = tuple(input("Enter tuple items separated by spaces: ").split())
start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))
print("Sliced tuple:", values[start:end])