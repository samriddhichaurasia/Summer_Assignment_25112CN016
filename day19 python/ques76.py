##find diagonal sum
# Step 1: Get the size of the square matrix from the user
n = int(input("Enter the number of rows/columns for the square matrix: "))

# Step 2: Initialize an empty list to store the matrix
matrix = []

# Step 3: Take matrix elements as input from the user row by row
print(f"Enter the elements row by row (press Enter after each number):")
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Element at [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

# Print the entered matrix for visual reference
print("\nThe entered matrix is:")
for row in matrix:
    print(row)

# Step 4: Initialize sum trackers for both diagonals
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

# Step 5: Loop through the matrix to calculate the diagonal sums
for i in range(n):
    # Primary diagonal condition: row index == column index (i == i)
    primary_diagonal_sum += matrix[i][i]
    
    # Secondary diagonal condition: column index == n - 1 - i
    secondary_diagonal_sum += matrix[i][n - 1 - i]

# Step 6: Print the final results
print(f"\nSum of Primary Diagonal: {primary_diagonal_sum}")
print(f"Sum of Secondary Diagonal: {secondary_diagonal_sum}")
print(f"Total Diagonal Sum: {primary_diagonal_sum + secondary_diagonal_sum}")
