#Reversing a List in Python

element = input("Enter the elementt: ")

reverse = ""

for elem in element[::-1]:
    reverse += elem + " "
print(reverse)
    