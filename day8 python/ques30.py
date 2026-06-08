##print number triangle pattern
rows=int(input("Enter the number of rows for the pattern: "))
for i in range(1,rows):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()