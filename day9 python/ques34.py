##reverse number triangle pattern
rows=int(input("Enter the number of rows for the pattern: "))
for i in range(rows,0,-1):
##-1 is used to decrement the value of i in each iteration, starting from rows and ending at 1.
    for j in range(1,i+1):
        print(j, end=" ")
    print()