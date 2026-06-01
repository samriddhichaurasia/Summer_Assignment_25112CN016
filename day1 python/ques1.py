# Take input from the user
n = int(input("Enter a number (n): "))

# Calculate sum using mathematical formula
# '//' is used for integer division to avoid a float output
total_sum = (n * (n + 1)) // 2

# Display the result
print(f"The sum of the first {n} numbers is: {total_sum}")
