#Find the sum of all items 
    #Input : {‘a’: 100, ‘b’:200, ‘c’:300}
    #Output : 600

Dictionary = int(input("Enter the No.of Items: "))

input_dict = {}

for i in range (Dictionary):
    
    Input_key = input("Enter the key: ")
    Input_value = float(input("Enter the value: "))
    
    input_dict[Input_key] = Input_value

    sum_dictionary = sum(input_dict.values())

print("Sum of the dictionary values is: ",sum_dictionary)




