#Convert a set into dictionary
    #initial string {1, 2, 3, 4, 5}
    #final list {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}


String = set(input("Enter the String: ").split())

ouptput = {element: 0 for  element in String}

print(ouptput)


