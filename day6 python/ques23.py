## count sets bits in a number
def count_set_bits_builtin(n):
    # Available in Python 3.10+
    return n.bit_count()

def count_set_bits_string(n):
    # Works in all Python versions
    return bin(n).count('1')

# Test the functions
num = 29  # Binary: 11101 (4 set bits)
print(f"Set bits in {num}: {count_set_bits_builtin(num)}")
print(f"Set bits in {num}: {count_set_bits_string(num)}")
