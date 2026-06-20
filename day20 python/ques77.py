##multiply matrices
# Step 1: Get dimensions for the first matrix
row1 = int(input("Enter the number of rows for Matrix 1: "))
col1 = int(input("Enter the number of columns for Matrix 1: "))

# Step 2: Get dimensions for the second matrix
row2 = int(input("Enter the number of rows for Matrix 2: "))
col2 = int(input("Enter the number of columns for Matrix 2: "))

# Step 3: Check if matrix multiplication is mathematically possible
if col1 != row2:
    print("\nError: Matrix multiplication is not possible!")
    print("The number of columns in Matrix 1 must equal the number of rows in Matrix 2.")
else:
    # Step 4: Take user input for Matrix 1
    print(f"\nEnter elements for Matrix 1 ({row1}x{col1}):")
    matrix1 = []
    for i in range(row1):
        row = []
        for j in range(col1):
            element = int(input(f"Enter element at position [{i}][{j}]: "))
            row.append(element)
        matrix1.append(row)

    # Step 5: Take user input for Matrix 2
    print(f"\nEnter elements for Matrix 2 ({row2}x{col2}):")
    matrix2 = []
    for i in range(row2):
        row = []
        for j in range(col2):
            element = int(input(f"Enter element at position [{i}][{j}]: "))
            row.append(element)
        matrix2.append(row)

    # Step 6: Initialize the result matrix with zeros (Dimensions: row1 x col2)
    result = []
    for i in range(row1):
        row = []
        for j in range(col2):
            row.append(0)
        result.append(row)

    # Step 7: Perform matrix multiplication using nested loops
    for i in range(row1):          # Loop through rows of Matrix 1
        for j in range(col2):      # Loop through columns of Matrix 2
            for k in range(col1):  # Loop through rows of Matrix 2 / columns of Matrix 1
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Step 8: Display the calculated result matrix
    print("\n--- Resulting Matrix ---")
    for row in result:
        print(*row)
