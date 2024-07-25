#Python program to find common elements in three lists using sets
     #Input :
       #ar1 = [1, 5, 10, 20, 40, 80]
       #ar2 = [6, 7, 20, 80, 100]
       #ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
     #Output : [80, 20]


list_1 = input("Enter the Set of Element.1: ")
list_2 = input("Enter the Set of Element.2: ")
list_3 = input("Enter the Set of Element.3: ")

set_1 = set(list_1)
print("Set_1",set_1)
set_2 = set(list_2)
print("Set_2",set_2)
set_3 = set(list_3)
print("Set_3",set_3)

Common_Element = sorted(set_1 & set_2 & set_3)

print("Common Elements in List: ",Common_Element)