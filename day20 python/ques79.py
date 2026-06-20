##find row wise sum
# Step 1: Get the matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Step 2: Initialize an empty list to store the matrix
matrix = []

# Step 3: Take matrix entries from the user row-wise
print("Enter the entries row-wise:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for position ({i},{j}): "))
        row.append(element)
    matrix.append(row)

# Step 4: Display the entered matrix
print("\nThe entered matrix is:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end="\t")
    print()

# Step 5: Calculate and print the row-wise sum manually
print("\nRow-wise sums:")
for i in range(rows):
    row_sum = 0  # Reset sum tracking for each row
    for j in range(cols):
        row_sum += matrix[i][j]  # Manually add each element
    print(f"Sum of Row {i + 1} = {row_sum}")
