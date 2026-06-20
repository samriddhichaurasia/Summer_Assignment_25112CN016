# Function to reverse the array
def reverse_array(arr):

    # Slicing with -1 reverses the array
    return arr[::-1]


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Call function
reversed_arr = reverse_array(arr)

# Display reversed array
print("Reversed Array:", reversed_arr)