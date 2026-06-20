# Function to rotate array left by one position
def rotate_left(arr):

    # First element moves to the end
    return arr[1:] + [arr[0]]


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
rotated_array = rotate_left(arr)

# Display result
print("Array after Left Rotation:")
print(rotated_array)