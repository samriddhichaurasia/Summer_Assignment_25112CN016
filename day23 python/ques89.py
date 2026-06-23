##find first non repeating character
# Take input from the user
text = input("Enter a string: ")

# Dictionary to store frequency of each character
freq = {}

# Count frequency of characters
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find the first non-repeating character
for ch in text:
    if freq[ch] == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found.")