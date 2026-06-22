##count vowels and consonants
# Accept string input from the user
text = input("Enter a string: ")

# Initialize counters
vowels_count = 0
consonants_count = 0

# Define a set of vowels for quick lookup
vowels_set = set("aeiou")

# Loop through each character in the string
for char in text.lower():
    #text.lower() helps to convert string into lowercase
    #char.isalpha() ensures that only actual letters are evaluated
    if char.isalpha():  # Check if the character is a letter
        if char in vowels_set:#checks if the letter belongs to the vowel collection
            vowels_count += 1
        else:
            consonants_count += 1

# Display the results
print(f"Total Vowels: {vowels_count}")
print(f"Total Consonants: {consonants_count}")
