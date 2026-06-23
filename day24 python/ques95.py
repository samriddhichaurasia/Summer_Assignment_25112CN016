##find longest word
user_input = input("Enter a sentence: ")
words = user_input.split()

if words:
    longest_word = ""
    
    # Loop through each word to compare lengths
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            
    print(f"The longest word is: '{longest_word}'")
else:
    print("No words found.")
