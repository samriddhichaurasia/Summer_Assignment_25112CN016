##merge two sorted arrays
def merge_sorted_arrays(arr1, arr2):
    """
    Merges two pre-sorted lists into a single sorted list 
    using the optimal two-pointer technique.
    """
    merged = []
    i, j = 0, 0
    n1, n2 = len(arr1), len(arr2)

    # Compare elements from both arrays and pick the smaller one
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append any remaining elements from the first array
    while i < n1:
        merged.append(arr1[i])
        i += 1

    # Append any remaining elements from the second array
    while j < n2:
        merged.append(arr2[j])
        j += 1

    return merged


# --- User Input Section ---
print("Note: Please enter the numbers in sorted order.")

# Take space-separated integer inputs for the first array
input1 = input("Enter elements of the 1st sorted array (separated by spaces): ")
array1 = [int(x) for x in input1.split() if x.strip()]

# Take space-separated integer inputs for the second array
input2 = input("Enter elements of the 2nd sorted array (separated by spaces): ")
array2 = [int(x) for x in input2.split() if x.strip()]

# Execute the merging algorithm
result = merge_sorted_arrays(array1, array2)

# Display the outcome
print("\n--- Results ---")
print(f"First Array:  {array1}")
print(f"Second Array: {array2}")
print(f"Merged Array: {result}")
