# Q20: Write a program to find the length of the longest word in a tuple.
words = tuple(input("Enter words separated by spaces: ").split())
longest_length = 0

for word in words:
    if len(word) > longest_length:
        longest_length = len(word)

print("Length of the longest word:", longest_length)