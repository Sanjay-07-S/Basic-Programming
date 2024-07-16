#Get a number input and print sum of all the number from 1 to the number.

n = int(input("Enter The Number: "))

sum_n = 0
addition = ""

for i in range (1,n+1):
    sum_n += i
    addition += str(i)
    
    if i != n:
        addition += "+"
print("Sum Of Numbers: ",addition)
print("Total Sum: ",sum_n)