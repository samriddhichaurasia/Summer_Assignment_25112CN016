##find maximum occuring character

# Input string from user
text = input("Enter a string: ")

# Dictionary to store frequency of each character
freq = {}

# Count frequency of each character
for ch in text:
    if ch in freq:
        freq[ch] += 1 #Checks if the character already exists in the dictionary.
    else:
        freq[ch] = 1#If the character appears for the first time, add it to the dictionary with count 1.

# Find character with maximum frequency
max_char = ''#stores the character with maximum occurrences
max_count = 0 # stores its frequency

for ch in freq:
    if freq[ch] > max_count: #Checks if the current character's frequency is greater than the current maximum.
        max_count = freq[ch]
        max_char = ch

# Display result
print("Maximum occurring character:", max_char)
print("Number of occurrences:", max_count)