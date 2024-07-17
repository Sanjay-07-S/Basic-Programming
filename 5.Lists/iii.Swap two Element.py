#Python Program to Swap Two Elements in a List.

Element = input("Enter the Element: ")

swap = Element.split()

index_1 =int(input("Enter index of element to swap: "))
index_2 =int(input("Enter indexx of element to swap: "))

if index_1 >= len(swap) or index_2>= len(swap):
    print("invalid")

else:
    swap[index_1], swap[index_2] = swap[index_2], swap[index_1]

print(swap)




