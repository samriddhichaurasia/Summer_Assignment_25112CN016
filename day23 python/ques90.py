##first repeating character
# Take input from the user
text = input("Enter a string: ")

# Set to store characters already seen
seen = set()

# Check each character
for ch in text:
    if ch in seen:
        print("First repeating character is:", ch)
        break
    seen.add(ch)
else:
    print("No repeating character found.")