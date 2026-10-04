# Q25: Count word frequency in a given paragraph using a dictionary.

paragraph = input("Enter a paragraph: ").lower()
words = paragraph.split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

print("Word frequencies:", frequency)