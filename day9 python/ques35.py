##repeated character pattern
rows=int(input("Enter the number of rows for the pattern: "))
for i in range(1,rows+1):
    for j in range(i):
        print(chr(65+i-1), end=" ")
    print()