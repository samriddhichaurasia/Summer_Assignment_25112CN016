# Python program to print prime numbers in a range

# Take input from the user for the range boundaries
lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

print(f"Prime numbers between {lower_bound} and {upper_bound} are:")

# Iterate through every number in the given range (inclusive)
for num in range(lower_bound, upper_bound + 1):
    # Prime numbers must be greater than 1
    if num > 1:
        # Check for factors from 2 up to the square root of the number
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break  # A factor is found, so it is not a prime number
        else:
            # The else block executes only if the loop finishes without breaking
            print(num, end=" ")
print()  # For a clean newline at the end
