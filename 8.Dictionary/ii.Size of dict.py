#Get size of a Dictionary in Python.

input_dict = {}

while True:
    Input_key = input("Enter the Key/ 'stop' to break: ")
    if Input_key == "stop":
        break
    Input_values = input("Enter the values: ")
    input_dict[Input_key] = Input_values

size_dict = len(input_dict)

print("Size of the dictionary:",size_dict)
print("Dictionary: ",input_dict)


