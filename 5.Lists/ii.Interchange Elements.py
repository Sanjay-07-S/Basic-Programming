# Python program to interchange first and last elements in a list.

Element = input("Enter the Elements: ")

elem = len(Element)
if elem > 1:
    first = Element[0]
    last = Element[-1]
    Element = last + Element[1:-1] + first

print(Element)




       
