    #write a python program to add two numbers given below a=55 and b=22
    #store the answer in a new variable
        #multiply the answer with a 
        #store the multiplied answer in new variable 
            #compare the multiplied answer with value a 
            #if the answer is greater then multiply the answer with (pi)value
            #increment the answer by 34
            #and decrement the answer by 20 
    #then compare the value of all the "present solution"

a = 55
b = 22
Sum = a+b
print("Added: ",Sum)
multiple = Sum*a
print("Multipled: ",multiple)
if multiple > a:
    compare = multiple*3.14
    print("compared: ", compare)
    increment = compare+34
    print("incremented: ",increment)
    decrement = compare-20
    print("decremented: ",decrement)
solution = Sum,multiple,compare,increment,decrement

sort_solution = sorted (solution)
print("sorted_solutions",sort_solution)