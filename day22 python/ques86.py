##count words in a sentence 
# Input sentence
sentence = input("enter sentence:")

# Split the sentence into a list of words
words_list = sentence.split()

# Initialize counter with 0
word_count = 0

# Loop through each word in the list
for word in words_list:
    word_count += 1

# Output the result
print("Total number of words:", word_count)
