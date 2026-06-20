##find column wise sum
# 1. Get the dimensions of the matrix from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# 2. Initialize an empty matrix
matrix = []

# 3. Take matrix elements as user input row by row
print("Enter the elements row-wise:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    matrix.append(row)

# 4. Display the entered matrix
print("\nThe entered matrix is:")
for row in matrix:
    for element in row:
        print(element, end="\t")
    print()

# 5. Calculate and display the column-wise sum
print("\nColumn-wise sums:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Sum of Column {j + 1}: {col_sum}")
