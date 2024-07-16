#Get a number input and print all the values from 1 to the number but skip values that are divisible by 10 - using continue.

n = int(input("Enter The Number: "))
for i in range(1,n+1):
    if n%10 ==0:
        continue
    print(i)