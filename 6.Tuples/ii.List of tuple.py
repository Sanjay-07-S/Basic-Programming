#Python program to create a list of tuples from given list having number and its cube in each tuple
    #Input: list = [1, 2, 3]
    #Output: [(1, 1), (2, 8), (3, 27)]

element = input("enter the elements: ")

list_tuple = list(map(int,element.split()))

cube_element = [(n,n **3) for n in list_tuple]

print(cube_element)
