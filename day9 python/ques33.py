##reverse star pattern
rows=int(input("Enter the number of rows for the pattern: "))
for i in range(rows,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()