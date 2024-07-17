#Reverse the words in the given string program using
    #Reverse method


String = input("Enter the Words: ")

words = String.split()

Reverse_word = "" 

words.reverse()
for word in words:
    Reverse_word += word + " "
print("Reversed Words Using Reverse Method: ", Reverse_word)