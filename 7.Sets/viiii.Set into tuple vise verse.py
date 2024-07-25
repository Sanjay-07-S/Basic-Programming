#Python program to convert Set into Tuple and Tuple into Set


Input_set  = set(input("Enter the String for set: ").split())
Input_tuple = tuple(input("Enter the String for tuple: ").split())


output_set = tuple(Input_set)
print("Convert from Set to Tuple: ",output_set)

output_tuple = set(Input_tuple)
print("Convert form Tuple to Set: ",output_tuple)


