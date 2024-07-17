#Reverse the words in the given string program using
    #Loop 

String = input("Enter a string: ")

words = String.split()

Reverse_word = ""
for word in words[::-1]:
    Reverse_word += word+" "
 
print("Reversed Words using loop:", Reverse_word)

