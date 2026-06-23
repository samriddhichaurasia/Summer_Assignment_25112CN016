##compress a string
def compress_string(text):
    if not text:
        return ""
    
    compressed = []
    current_char = text[0]
    count = 1
    
    # Loop through the string starting from the second character
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            # Append the character and its frequency
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
            
    # Append the last character group
    compressed.append(f"{current_char}{count}")
    
    # Join list into a string
    result = "".join(compressed)
    
    # Return original string if compression didn't make it smaller
    return result if len(result) < len(text) else text

# Example Usage
input_str = input("enter string:")
print("Original:", input_str)
print("Compressed:", compress_string(input_str))
