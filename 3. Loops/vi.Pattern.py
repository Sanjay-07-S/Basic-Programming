#Print the following pattern using loops
    #1 
    #2 2 
    #3 3 3 
    #4 4 4 4

n = int(input("Enter The Number: "))
for i in range(1,n+1):
    for j in range(i):
        print(i, end="")
    print()