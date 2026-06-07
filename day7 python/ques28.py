##recursive reverse Number
def reverse_number(n):
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** (len(str(n)) - 1)) + reverse_number(n // 10)
num = int(input("Enter a number: "))
print(f"The reverse of {num} is: {reverse_number(num)}")
