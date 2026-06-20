# Function to find the element having maximum frequency
def max_frequency(arr):

    # Assume first element has maximum frequency
    max_freq = 0
    element = arr[0]

    # Check frequency of each element
    for num in arr:

        freq = arr.count(num)

        # Update if higher frequency found
        if freq > max_freq:
            max_freq = freq
            element = num

    # Return both element and frequency
    return element, max_freq


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
element, freq = max_frequency(arr)

# Display result
print("Maximum Frequency Element =", element)
print("Frequency =", freq)