# Function to perform Bubble Sort
def bubble_sort(arr):

    n = len(arr)

    # Outer loop for passes
    for i in range(n):

        # Inner loop for comparison
        for j in range(0, n - i - 1):

            # Swap if current element is greater
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
sorted_arr = bubble_sort(arr)

print("Sorted Array:", sorted_arr)