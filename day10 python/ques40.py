## print alphabet pyramid pattern
rows=int(input("Enter the number of rows for the pattern: "))
for i in range(1, rows + 1):
    spaces=" " * (rows - i)
    print(spaces, end="")
    for j in range(1,i + 1):
    ## j is used for spaces
        print(chr(64 + j), end=" ")
    for k in range(i-1,0,-1):
    ## k is used for characters
        print(chr(64 + k), end=" ")
    print()