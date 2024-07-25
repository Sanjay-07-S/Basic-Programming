#Convert Set to String in Python and vice-versa

String = input("Enter the string: ").split()

input_set = set(String)
print("initial set: ",input_set)
output_set = ','.join(input_set)
print("Convert form Set to String:",output_set)

input_string = set(output_set.split(','))
print("Convert from String to Set:",input_string)