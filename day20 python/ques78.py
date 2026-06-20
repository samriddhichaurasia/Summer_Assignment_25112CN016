##check symmetric matrix
# Step 1: Take row and column dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# A matrix can only be symmetric if it is a square matrix
if rows != cols:
    print("\nThe matrix must be square (rows must equal columns) to be symmetric.")
else:
    # Step 2: Initialize an empty list to store the matrix
    matrix = []
    print(f"\nEnter the elements for a {rows}x{cols} matrix row by row:")
    
    # Take matrix elements as user input
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

    # Step 3: Print the entered matrix for verification
    print("\nYour Matrix:")
    for row in matrix:
        print(row)

    # Step 4: Check for symmetry
    is_symmetric = True
    
    for i in range(rows):
        # Optimizing to check only the elements above the diagonal (j > i)
        for j in range(i + 1, cols):
            if matrix[i][j] != matrix[j][i]:
                is_symmetric = False
                break  # Break inner loop if mismatch is found
        if not is_symmetric:
            break  # Break outer loop if mismatch is found

    # Step 5: Display the final result
    if is_symmetric:
        print("\nResult: The matrix IS a symmetric matrix.")
    else:
        print("\nResult: The matrix IS NOT a symmetric matrix.")
