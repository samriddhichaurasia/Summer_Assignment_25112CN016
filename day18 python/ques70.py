# Function to perform Selection Sort
def selection_sort(arr):

    n = len(arr)

    # Traverse entire array
    for i in range(n):

        # Assume current position has minimum value
        min_index = i

        # Find actual minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap minimum element with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
sorted_arr = selection_sort(arr)

print("Sorted Array:", sorted_arr)