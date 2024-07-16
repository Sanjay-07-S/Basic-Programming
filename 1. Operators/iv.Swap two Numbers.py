#write a python program to swap two numbers
# input format
#    a=4
#    b=9
# output format 
#    a=9
#    b=4


a = float(input("Enter A: "))
b = float(input("Enter B: "))
a,b = b,a
print("a",a)
print("b",b)