#Difference between two lists
    #list1 = [10, 15, 20, 25, 30, 35, 40]
    #list2 = [25, 40, 35]
    #Output: [10, 15, 20, 30]

list_1 = input("Enter the List Elements.1: ")
list_2 = input("Enter the List elements.2: ")


set_1 = set(list_1)
set_2 = set(list_2)

Difference= list(set_1 - set_2)

print("Difference Between Two List: ",Difference)