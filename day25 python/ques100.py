##sort words by length
# Get input from the user
user_input = input("Enter a sentence: ")

# Split the sentence into words manually without built-in split()
words = []
current_word = ""
for char in user_input:
    if char == " ":
        if current_word:
            words.append(current_word)
            current_word = ""
    else:
        current_word += char
if current_word:
    words.append(current_word)

# Sort the words by length using Bubble Sort algorithm
num_words = len(words)
for i in range(num_words):
    for j in range(0, num_words - i - 1):
        # Compare lengths of adjacent words
        if len(words[j]) > len(words[j + 1]):
            # Swap the words if the first is longer than the second
            words[j], words[j + 1] = words[j + 1], words[j]

# Display the sorted words
print("Words sorted by length:")
for word in words:
    print(word)
