##
# Step 1: Take matrix dimensions as input from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Step 2: Initialize empty lists for the matrices
matrix_A = []
matrix_B = []
result_matrix = []

# Step 3: Take user input for the First Matrix (Matrix A)
print("\nEnter elements for the First Matrix (Matrix A):")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element A[{i}][{j}]: "))
        row.append(element)
    matrix_A.append(row)

# Step 4: Take user input for the Second Matrix (Matrix B)
print("\nEnter elements for the Second Matrix (Matrix B):")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element B[{i}][{j}]: "))
        row.append(element)
    matrix_B.append(row)

# Step 5: Perform matrix addition and store the values in the result matrix
for i in range(rows):
    row = []
    for j in range(cols):
        # Add corresponding elements from both matrices
        sum_element = matrix_A[i][j] + matrix_B[i][j]
        row.append(sum_element)
    result_matrix.append(row)

# Step 6: Print the resulting sum matrix in a structured format
print("\nThe Resultant Matrix after Addition is:")
for row in result_matrix:
    for element in row:
        print(element, end=" ")
    print()  # Move to the next line after printing a full row
