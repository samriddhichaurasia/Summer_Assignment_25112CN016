##check anagram strings
# Take input from the user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Compare sorted characters
if sorted(str1) == sorted(str2):
    print("The strings are Anagrams.")
else:
    print("The strings are not Anagrams.")