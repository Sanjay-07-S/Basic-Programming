#Reverse the words in the given string program using
    #Stack
    
String = input("Enter a string: ")

words = String.split()

stack = []
Reverse_word =" "
for word in words:
    stack.append(word)

while stack:
    Reverse_word +=  stack.pop() + " "

print("Reversed Words using stack:",Reverse_word )
