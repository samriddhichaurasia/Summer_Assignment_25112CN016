##Transpose matrix
# Step 1: Get the matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Step 2: Initialize an empty list to store the original matrix
matrix = []

# Step 3: Take matrix elements as input from the user row by row
print("Enter the elements row-wise:")
for i in range(rows):
    row_elements = []
    for j in range(cols):
        element = int(input(f"Enter element for position [{i}][{j}]: "))
        row_elements.append(element)
    matrix.append(row_elements)

# Step 4: Print the original matrix
print("\nOriginal Matrix:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

# Step 5: Initialize a result matrix filled with zeros
# The dimensions are swapped: new rows = original cols, new cols = original rows
transpose = [[0 for _ in range(rows)] for _ in range(cols)]

# Step 6: Perform the transposition operation using nested loops
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = matrix[i][j]

# Step 7: Print the transposed matrix
print("\nTransposed Matrix:")
for i in range(cols):
    for j in range(rows):
        print(transpose[i][j], end=" ")
    print()
