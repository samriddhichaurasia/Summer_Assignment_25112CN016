##sort names alphabetically
## by using bubble sorting
# 1. Take a list of names as input from the user
user_input = input("Enter names separated by spaces: ")

# 2. Split the input string into a list of individual names manually
names = user_input.split()

# Get the total number of names
n = len(names)

# 3. Implement Bubble Sort to arrange names alphabetically
for i in range(n):
    for j in range(0, n - i - 1):
        # To make it case-insensitive, we compare lowercase versions of the names
        if names[j].lower() > names[j + 1].lower():
            # Swap the names if they are in the wrong order
            names[j], names[j + 1] = names[j + 1], names[j]

# 4. Display the sorted names
print("\nNames in alphabetical order:")
for name in names:
    print(name)
