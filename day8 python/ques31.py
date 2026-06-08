##print alphabet pattern
rows=int(input("Enter the number of rows for the pattern: "))
for i in range(rows):
    for j in range(i+1):
        print(chr(65+j), end=" ")
    print()