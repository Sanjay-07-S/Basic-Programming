#Check if two lists have at-least one element common
 #Input : a = [1, 2, 3, 4, 5]
  #b = [5, 6, 7, 8, 9]
 #Output : True


List_1 = input("Enter list of Element.1 :")
List_2 = input("Enter list of Element.2 :")

Set_1 = set(List_1)
Set_2 = set(List_2)

common = list(Set_1 & Set_2)

Common_element = bool(common)

print("is there any atleast one common element: ",Common_element)