##check string rotation
#concatenate the first string with itself and check if the second string exists inside it
def is_string_rotation(str1, str2):
    # Check if lengths match and are not empty
    if len(str1) != len(str2) or not str1:
        return False
    
    # Concatenate str1 with itself
    temp_str = str1 + str1
    
    # Check if str2 is a substring of the doubled string
    return str2 in temp_str

# --- Driver Code ---
string1 = input("enter string 1:")
string2 = input("enter string 2:")

if is_string_rotation(string1, string2):
    print(f"'{string2}' is a valid rotation of '{string1}'")
else:
    print(f"'{string2}' is NOT a valid rotation of '{string1}'")
