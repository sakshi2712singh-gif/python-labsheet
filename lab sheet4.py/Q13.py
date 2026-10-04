# Q13: Count the frequency of characters in a string using a dictionary.

text = input("Enter a string: ")
frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("Character frequencies:", frequency)