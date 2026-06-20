# Function to rotate array right by one position
def rotate_right(arr):

    # Last element comes to first position
    return [arr[-1]] + arr[:-1]


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
rotated_array = rotate_right(arr)

# Display result
print("Array after Right Rotation:")
print(rotated_array)