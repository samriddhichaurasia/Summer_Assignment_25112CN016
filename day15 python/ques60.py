# Function to move all zeroes to the end
def move_zeroes(arr):

    # Store all non-zero elements
    non_zero = []

    # Store all zero elements
    zeroes = []

    # Traverse the array
    for num in arr:

        # Separate non-zero and zero values
        if num == 0:
            zeroes.append(num)
        else:
            non_zero.append(num)

    # Combine both lists
    return non_zero + zeroes


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
result = move_zeroes(arr)

# Display modified array
print("Array after moving zeroes:")
print(result)