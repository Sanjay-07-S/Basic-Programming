#Reverse the words in the given string program using
    #slicing

String = input("Enter the Words: ")

words = String.split()

Reverse_word = ""

for word in words[::-1]:
    Reverse_word += word + " "

print("Reversed Words using Slicing:",Reverse_word)
